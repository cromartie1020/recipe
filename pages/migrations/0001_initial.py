# Generated by Django 5.0.3 on 2024-09-12 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('measure', models.CharField(choices=[('OZ', 'ounces'), ('GM', 'grams'), ('L', 'liters'), ('LB', 'pounds'), ('CUP', 'cups'), ('DR', 'drams')], default='ounces', max_length=20)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ingredient')),
            ],
            options={
                'verbose_name_plural': 'recipies',
                'ordering': ['-name'],
            },
        ),
    ]
