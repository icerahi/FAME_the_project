# Generated by Django 2.2 on 2019-07-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_delete_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
