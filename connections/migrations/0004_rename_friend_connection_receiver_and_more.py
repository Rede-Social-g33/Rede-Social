# Generated by Django 4.0.7 on 2023-03-13 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_alter_connection_friendship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connection',
            old_name='friend',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='connection',
            old_name='user',
            new_name='sender',
        ),
    ]
