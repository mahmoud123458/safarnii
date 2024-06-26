# Generated by Django 5.0.1 on 2024-02-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="places",
            name="image",
            field=models.ImageField(default="", upload_to="home/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="places",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
