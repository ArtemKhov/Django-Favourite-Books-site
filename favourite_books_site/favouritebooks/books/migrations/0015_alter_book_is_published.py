# Generated by Django 5.1.1 on 2024-10-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_book_author_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(choices=[(1, 'Published (available for all to view)'), (0, 'Not Published (available only you)')], default=1),
        ),
    ]
