# Generated by Django 5.0.3 on 2024-03-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trollapp', '0006_alter_lobby_lobby_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lobby',
            name='lobby_id',
        ),
        migrations.AddField(
            model_name='lobby',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
