# Generated by Django 4.2.3 on 2023-09-03 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='CNName',
            new_name='CName',
        ),
    ]
