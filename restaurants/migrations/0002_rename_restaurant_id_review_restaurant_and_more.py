# Generated by Django 4.0.10 on 2024-10-14 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]
