# Generated by Django 3.2.7 on 2021-11-20 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uploaded_by',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
