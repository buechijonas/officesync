# Generated by Django 4.2.4 on 2023-09-15 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeSync',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, default='OfficeSync', max_length=20, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='authentication/static/images/uploads/logo')),
            ],
        ),
        migrations.CreateModel(
            name='Warn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('Falschinformationen', 'Falschinformationen'), ('Missbrauch von Privilegien', 'Missbrauch von Privilegien'), ('Belästigung', 'Belästigung'), ('Cybermobbing', 'Cybermobbing'), ('Cybergrooming', 'Cybergrooming'), ('Whataboutismus', 'Whataboutismus'), ('Relativierung', 'Relativierung'), ('Erpressung', 'Erpressung'), ('Drohung', 'Drohung'), ('Wortwahl', 'Wortwahl'), ('Hassrede', 'Hassrede'), ('Beleidugung', 'Beleidigung'), ('Diskriminierung', 'Diskriminierung'), ('Sexismus', 'Sexismus'), ('Rassismus', 'Rassismus'), ('Faschismus', 'Faschismus'), ('Antisemitismus', 'Antisemitismus'), ('Betrug', 'Betrug'), ('Spam', 'Spam')], default='Hassrede', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warns', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCustomInterface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ui', models.CharField(choices=[('Hell', 'Hell'), ('Dunkel', 'Dunkel'), ('Kontrast', 'Kontrast')], default='Hell', max_length=50)),
                ('gender', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_custom_interface', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdvancedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp', models.ImageField(blank=True, null=True, upload_to='static/images/uploads/profile')),
                ('privacy', models.BooleanField(default=False)),
                ('terms', models.BooleanField(default=False)),
                ('copyright', models.BooleanField(default=False)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='administration.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advanced', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]