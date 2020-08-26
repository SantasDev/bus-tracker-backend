# Generated by Django 3.0.8 on 2020-08-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200810_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btuser',
            old_name='location',
            new_name='contract',
        ),
        migrations.AddField(
            model_name='btuser',
            name='enterprise',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='btuser',
            name='role',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
