# Generated by Django 4.0.4 on 2022-05-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_list', '0005_tariff_yandex_alter_tariff_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='technology',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
