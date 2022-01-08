# Generated by Django 4.0.1 on 2022-01-08 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('model_location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('phone_number', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('floor_of_flat', models.CharField(max_length=255)),
                ('number_of_rooms', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='model_location.city')),
            ],
            options={
                'verbose_name': 'flat',
                'verbose_name_plural': 'flats',
            },
        ),
    ]
