# Generated by Django 3.1.6 on 2021-06-16 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagementApp', '0003_auto_20210613_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tododb',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='tododb',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='tododb',
            name='timetaken',
        ),
    ]