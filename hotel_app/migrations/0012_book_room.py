# Generated by Django 4.2.11 on 2024-06-06 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0011_remove_book_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotel_app.addroom'),
        ),
    ]
