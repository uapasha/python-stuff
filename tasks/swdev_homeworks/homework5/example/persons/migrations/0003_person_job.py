# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('persons', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='job',
            field=models.ForeignKey(default=b'3520', verbose_name=b'Job description', to='jobs.Job'),
        ),
    ]
