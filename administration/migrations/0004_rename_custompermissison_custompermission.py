# Generated by Django 4.2.4 on 2023-08-16 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_custompermissison_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomPermissison',
            new_name='CustomPermission',
        ),
    ]