# Generated by Django 4.2 on 2023-04-25 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list_created_at'),
        ('tags', '0003_remove_tag_created_at'),
        ('places', '0002_alter_place_slug'),
        ('memos', '0002_rename_creted_at_memo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='lists',
            field=models.ManyToManyField(to='lists.list'),
        ),
        migrations.AlterField(
            model_name='memo',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
        migrations.AlterField(
            model_name='memo',
            name='tags',
            field=models.ManyToManyField(to='tags.tag'),
        ),
    ]
