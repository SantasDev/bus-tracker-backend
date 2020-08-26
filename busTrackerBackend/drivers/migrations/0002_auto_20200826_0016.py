# Generated by Django 3.0.8 on 2020-08-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busdriver',
            name='bus_id',
        ),
        migrations.RemoveField(
            model_name='busdriver',
            name='enterprice_id',
        ),
        migrations.RemoveField(
            model_name='busdriver',
            name='route_id',
        ),
        migrations.RemoveField(
            model_name='busdriver',
            name='user_id',
        ),
        migrations.AddField(
            model_name='busdriver',
            name='license_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='busdriver',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
