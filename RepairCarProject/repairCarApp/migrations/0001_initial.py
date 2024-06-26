# Generated by Django 5.0.6 on 2024-06-06 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('country', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('yearEst', models.IntegerField()),
                ('oldTimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('maxSpeed', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairCarApp.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='cover_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairCarApp.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairCarApp.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopsManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairCarApp.manufacturer')),
                ('workshops', models.ManyToManyField(to='repairCarApp.workshop')),
            ],
        ),
    ]
