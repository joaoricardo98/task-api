# Generated by Django 3.1.5 on 2021-01-22 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=500)),
                ('status', models.SmallIntegerField(choices=[(1, 'Pendente'), (2, 'Feito')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task.user')),
            ],
        ),
    ]
