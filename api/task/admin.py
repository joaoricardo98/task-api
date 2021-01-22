from django.contrib import admin

from task.models import User
from task.models import Task


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 20


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status')
    list_display_links = ('id', 'description')
    search_fields = ('id', )
    list_per_page = 20


admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
