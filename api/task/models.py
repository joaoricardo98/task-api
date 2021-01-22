from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import SmallIntegerField


class User(Model):
    name = CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - {self.name}'

    def delete(self, *args, **kwargs):
        Task.objects.filter(user=self.id).delete()
        return super().delete(*args, **kwargs)


class Task(Model):
    STATUS_CHOICES = (
        (1, 'Pendente'),
        (2, 'Feito')
    )

    description = CharField(max_length=500, blank=False, null=False, default='')
    status = SmallIntegerField(blank=False, choices=STATUS_CHOICES, null=False, default=1)
    user = ForeignKey(User, on_delete=PROTECT, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - {self.user.id}'



