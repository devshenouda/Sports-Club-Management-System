# Generated by Django 5.1.4 on 2024-12-26 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0003_rename_category_team_type_team_players_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='team_name',
        ),
    ]
