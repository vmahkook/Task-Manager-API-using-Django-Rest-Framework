from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Task
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value.strip()
