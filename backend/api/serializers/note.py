from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
