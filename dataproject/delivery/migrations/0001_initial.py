# Generated by Django 3.1.1 on 2022-12-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitDatabase',
            fields=[
                ('username_primary_key', models.CharField(help_text='User id must be unique', max_length=30, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('order_name', models.CharField(max_length=20)),
                ('coupon_code', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
    ]
