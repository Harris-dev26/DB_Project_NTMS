# Generated by Django 4.1.4 on 2022-12-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourists', '0017_alter_bookings_edate_alter_bookings_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='Package',
            field=models.CharField(choices=[('premium', 'Premium'), ('middle', 'Middle'), ('budget', 'Budget')], default='', max_length=120),
        ),
    ]
