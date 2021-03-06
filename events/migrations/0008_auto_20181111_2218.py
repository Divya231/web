# Generated by Django 2.1.2 on 2018-11-11 22:18

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    WaitingList = apps.get_model('events', 'Refund')
    for wl in WaitingList.objects.all():
        wl.sell_code = uuid.uuid4()
        wl.save()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_waitinglist_buy_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='sell_code',
            field=models.UUIDField(default=None, blank=True, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='refund',
            name='sell_code',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
