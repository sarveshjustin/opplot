# Generated by Django 3.1.1 on 2022-12-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitdatabase',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
