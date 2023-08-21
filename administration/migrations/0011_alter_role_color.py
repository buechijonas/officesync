# Generated by Django 4.2.4 on 2023-08-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_alter_role_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='color',
            field=models.CharField(choices=[('darkred', 'Dunkelrot'), ('red', 'Rot'), ('darkorange', 'Dunkelorange'), ('orange', 'Orange'), ('lightgreen', 'Hellgrün'), ('darkgreen', 'Dunkelgrün'), ('darkcyan', 'Türkis'), ('lightblue', 'Hellblau'), ('darkblue', 'Dunkelblau'), ('mediumpurple', 'Violett'), ('hotpink', 'Rosa'), ('gray', 'Grau'), ('brown', 'Braun'), ('black', 'Schwarz')], default='black', max_length=20),
        ),
    ]