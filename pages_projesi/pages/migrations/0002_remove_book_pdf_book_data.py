# Generated by Django 4.1.6 on 2023-02-22 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="pdf",),
        migrations.AddField(
            model_name="book",
            name="data",
            field=models.FileField(
                default=django.utils.timezone.now, upload_to="books/data/"
            ),
            preserve_default=False,
        ),
    ]
