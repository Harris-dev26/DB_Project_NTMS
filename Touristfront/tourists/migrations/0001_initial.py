# Generated by Django 4.1.3 on 2022-11-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.CharField(max_length=120, verbose_name='hotel ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('password', models.CharField(max_length=120, verbose_name='password')),
                ('location_id', models.CharField(max_length=120, verbose_name='Location')),
                ('a_rooms', models.IntegerField(max_length=120, verbose_name='available rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Locals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.CharField(max_length=120, verbose_name='Local ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='first name')),
                ('second_name', models.CharField(max_length=120, verbose_name='last name')),
                ('location', models.CharField(max_length=120, verbose_name='location')),
                ('number', models.IntegerField(verbose_name='phone number')),
                ('password', models.CharField(max_length=120, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120, verbose_name='Tourist ID')),
                ('cnic', models.IntegerField(verbose_name='CNIC')),
                ('first_name', models.CharField(max_length=120, verbose_name='first name')),
                ('las_name', models.CharField(max_length=120, verbose_name='last name')),
                ('location', models.CharField(max_length=120, verbose_name='location')),
                ('password', models.CharField(max_length=120, verbose_name='password')),
                ('book_id', models.CharField(max_length=120, verbose_name='booking ID')),
                ('number', models.IntegerField(verbose_name='phone number')),
            ],
        ),
    ]
