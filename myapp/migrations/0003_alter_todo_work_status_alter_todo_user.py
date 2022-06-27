# Generated by Django 4.0.4 on 2022-06-26 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_rename_todolist_todo_title_todo_date_alter_todo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Work_Status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
