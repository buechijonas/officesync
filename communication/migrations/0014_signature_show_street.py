# Generated by Django 3.2.20 on 2023-11-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0013_auto_20231106_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='show_street',
            field=models.BooleanField(default=True, verbose_name='Strasse anzeigen'),
        ),
    ]