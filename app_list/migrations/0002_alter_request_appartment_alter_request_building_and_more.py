# Generated by Django 4.0.4 on 2022-05-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='appartment',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='building',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='region',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='street',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
