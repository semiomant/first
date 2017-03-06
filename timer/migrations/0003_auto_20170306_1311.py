# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0002_auto_20170306_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerdata',
            name='rest_url',
            field=models.CharField(verbose_name='GET url', max_length=255, default='/api/clock/now?format=json', help_text='url für REST api'),
        ),
    ]
