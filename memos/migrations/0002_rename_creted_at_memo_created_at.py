# Generated by Django 4.2 on 2023-04-24 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='creted_at',
            new_name='created_at',
        ),
    ]
