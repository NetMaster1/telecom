# Generated by Django 4.0.4 on 2022-05-25 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_list', '0011_alter_channel_thumbnail_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='appartment',
        ),
        migrations.RemoveField(
            model_name='request',
            name='l_name',
        ),
    ]
