# Generated by Django 2.0.4 on 2019-05-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_development', '0002_callsession__lending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callsession',
            name='_lending',
            field=models.BooleanField(default=False),
        ),
    ]
