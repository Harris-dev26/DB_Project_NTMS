# Generated by Django 4.1.3 on 2022-12-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='Package',
            field=models.CharField(choices=[('premium', 'Premium'), ('middle', 'Middle'), ('budget', 'Budget')], default='', max_length=120),
        ),
    ]
