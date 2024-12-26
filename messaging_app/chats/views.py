from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.prefetch_related('participants', 'messages')
    serializer_class = ConversationSerializer

    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        """
        Endpoint to create a new conversation.
        Expects a list of participant IDs in the request data.
        """
        participant_ids = request.data.get('participants', [])
        if not participant_ids:
            return Response({"error": "Participants are required."}, status=status.HTTP_400_BAD_REQUEST)

        participants = User.objects.filter(user_id__in=participant_ids)
        if not participants.exists():
            return Response({"error": "Invalid participant IDs."}, status=status.HTTP_400_BAD_REQUEST)

        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related('sender', 'conversation')
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        """
        Endpoint to send a message to an existing conversation.
        Expects `conversation_id` and `message_body` in the request data.
        """
        conversation_id = request.data.get('conversation_id')
        message_body = request.data.get('message_body')

        if not conversation_id or not message_body:
            return Response({"error": "conversation_id and message_body are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)

        message = Message.objects.create(
            sender=request.user,  # Assuming authentication is set up and the user is logged in
            conversation=conversation,
            message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
