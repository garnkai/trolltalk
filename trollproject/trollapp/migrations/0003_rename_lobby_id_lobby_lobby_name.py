# Generated by Django 5.0.1 on 2024-03-24 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trollapp', '0002_lobby_game_mode_lobby_num_players_lobby_privacy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lobby',
            old_name='lobby_id',
            new_name='lobby_name',
        ),
    ]
