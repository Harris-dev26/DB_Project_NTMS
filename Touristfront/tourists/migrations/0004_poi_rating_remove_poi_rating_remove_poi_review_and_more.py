# Generated by Django 4.1.3 on 2022-11-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourists', '0003_remove_poi_poi_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='POI_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('Rating', models.IntegerField(max_length=30, verbose_name=' rating ')),
                ('Review', models.CharField(max_length=30, verbose_name=' review ')),
            ],
        ),
        migrations.RemoveField(
            model_name='poi',
            name='Rating',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='Review',
        ),
        migrations.AddField(
            model_name='poi',
            name='Rating_Review',
            field=models.ManyToManyField(blank=True, to='tourists.poi_rating'),
        ),
    ]
