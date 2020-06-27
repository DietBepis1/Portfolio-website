# Generated by Django 3.0.7 on 2020-06-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_showcase', '0008_showcaseitem_path_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showcaseitem',
            old_name='path_to',
            new_name='path_to_git',
        ),
        migrations.AddField(
            model_name='showcaseitem',
            name='path_to_site',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]