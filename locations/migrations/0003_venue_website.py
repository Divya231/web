# Generated by Django 2.2.4 on 2019-08-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20180827_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]