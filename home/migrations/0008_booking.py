# Generated by Django 5.0.4 on 2024-05-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_places_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
        ),
    ]
