from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import FriendRequest, Message

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer()

    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'is_accepted', 'timestamp']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']