# Generated by Django 2.2.7 on 2019-12-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20191201_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='fee_received_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
