from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from task.models import User
from task.models import Task
from task.serializers import UserSerializer
from task.serializers import TaskByUserSerializer
from task.serializers import TaskSerializer


class UserViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskByUserList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskByUserSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        queryset = self.queryset.filter(user=user_id)

        return queryset


class TaskViewSet(
    RetrieveModelMixin, CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



