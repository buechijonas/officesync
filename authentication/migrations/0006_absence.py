# Generated by Django 3.2.20 on 2023-12-27 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0005_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Urlaub', 'urlaub'), ('Krankheit', 'krankheit'), ('Sonstiges', 'sonstiges')], max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('confirmation', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_absences', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_absences', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='absences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start'],
            },
        ),
    ]