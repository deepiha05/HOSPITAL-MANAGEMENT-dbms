# Generated by Django 4.1.7 on 2023-03-03 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_remove_test_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='appoitmentID',
        ),
    ]
