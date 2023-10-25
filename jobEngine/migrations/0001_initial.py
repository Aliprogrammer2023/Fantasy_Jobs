# Generated by Django 4.2.5 on 2023-10-06 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('linkedIn', models.CharField(blank=True, max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(max_length=10000)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobEngine.profile')),
            ],
        ),
    ]
