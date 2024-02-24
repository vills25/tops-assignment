from rest_framework import serializers
from .models import Task

class tasks_serializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']