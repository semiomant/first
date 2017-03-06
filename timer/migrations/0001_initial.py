# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimerData',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, related_name='timer_timerdata', to='cms.CMSPlugin', serialize=False, primary_key=True)),
                ('haha', models.CharField(verbose_name='Schrumdeidei', help_text='stuff1', max_length=255)),
                ('lala', models.CharField(verbose_name='zeuch', help_text='stuff2', max_length=255)),
                ('dudu', models.CharField(verbose_name='dingsda', help_text='stuff3', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
