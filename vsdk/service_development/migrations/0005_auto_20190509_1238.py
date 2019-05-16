# Generated by Django 2.1.7 on 2019-05-09 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_development', '0004_auto_20190508_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='offer',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service_development.KasaDakaUser', verbose_name='Caller_id'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Product', verbose_name='Product label'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Region', verbose_name='Product label'),
        ),
    ]