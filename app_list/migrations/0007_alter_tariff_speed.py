# Generated by Django 4.0.4 on 2022-05-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_list', '0006_alter_tariff_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='speed',
            field=models.CharField(default='100 Мб/сек', max_length=10),
        ),
    ]
