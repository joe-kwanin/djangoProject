# Generated by Django 4.0.1 on 2022-12-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmManager', '0002_alter_records_age_alter_records_date_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='egg_production',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='records',
            name='feed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='records',
            name='no_birds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='records',
            name='total_stock',
            field=models.IntegerField(null=True),
        ),
    ]
