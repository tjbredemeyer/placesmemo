# Generated by Django 4.2 on 2023-04-25 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_taggedmemo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='created_at',
        ),
    ]