# Generated by Django 5.1.1 on 2024-10-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
