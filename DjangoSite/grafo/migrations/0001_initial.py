# Generated by Django 3.2.7 on 2021-11-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R1', models.IntegerField()),
                ('R2', models.IntegerField()),
                ('D', models.FloatField()),
                ('YN', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Distance',
                'verbose_name_plural': 'Distances',
            },
        ),
    ]
