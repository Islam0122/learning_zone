# Generated by Django 5.2.3 on 2025-06-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year_built', models.DateField()),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
