# Generated by Django 3.1.4 on 2021-01-19 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('new_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 1, 19, 16, 26, 8, 719913, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 19, 16, 26, 8, 719913, tzinfo=utc)),
        ),
    ]