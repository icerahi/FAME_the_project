# Generated by Django 2.2 on 2019-07-19 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='followed',
        ),
    ]
