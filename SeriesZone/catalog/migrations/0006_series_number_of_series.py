# Generated by Django 4.2.2 on 2023-06-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_series_number_of_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='number_of_series',
            field=models.IntegerField(default=1),
        ),
    ]
