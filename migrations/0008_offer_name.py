# Generated by Django 2.1.7 on 2019-05-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_development', '0007_auto_20190509_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]