# Generated by Django 4.1.6 on 2023-06-16 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_date_of_issue_serial_dateofissue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='number_of_series',
        ),
    ]
