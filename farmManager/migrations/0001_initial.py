# Generated by Django 4.0.1 on 2022-12-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pen_no', models.CharField(max_length=100)),
                ('production_type', models.CharField(max_length=200)),
                ('date_received', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('no_birds', models.IntegerField()),
                ('feed', models.IntegerField()),
                ('egg_production', models.IntegerField()),
                ('total_stock', models.IntegerField()),
                ('medication', models.CharField(max_length=700)),
                ('remarks', models.CharField(max_length=700)),
            ],
        ),
    ]