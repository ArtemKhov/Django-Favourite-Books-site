# Generated by Django 5.1.1 on 2024-10-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]