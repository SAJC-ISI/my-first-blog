# Generated by Django 3.2.7 on 2021-11-26 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grafo', '0003_distance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distance',
            old_name='D',
            new_name='distance',
        ),
        migrations.RemoveField(
            model_name='distance',
            name='YN',
        ),
    ]
