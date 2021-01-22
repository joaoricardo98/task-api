from rest_framework import serializers

from task.models import User
from task.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'id']
        model = User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'description', 'status', 'user']
        model = Task


class TaskByUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['description', 'status']
        model = Task
