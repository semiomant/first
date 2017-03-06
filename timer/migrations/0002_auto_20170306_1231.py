# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timerdata',
            name='dudu',
        ),
        migrations.RemoveField(
            model_name='timerdata',
            name='haha',
        ),
        migrations.RemoveField(
            model_name='timerdata',
            name='lala',
        ),
        migrations.AddField(
            model_name='timerdata',
            name='background',
            field=models.CharField(help_text='background color name', default='white', max_length=255, verbose_name='background color'),
        ),
        migrations.AddField(
            model_name='timerdata',
            name='interval',
            field=models.IntegerField(help_text='interval in s', default=60, verbose_name='Interval'),
        ),
        migrations.AddField(
            model_name='timerdata',
            name='rest_url',
            field=models.CharField(help_text='url für REST api', default='api/clock/now?format=json', max_length=255, verbose_name='GET url'),
        ),
    ]
