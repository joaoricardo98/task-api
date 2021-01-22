from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from task.views import TaskByUserList
from task.views import TaskViewSet
from task.views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='Usuarios')
router.register(r'tasks', TaskViewSet, basename='Task')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'users/<int:pk>/tasks/', TaskByUserList.as_view())
]
