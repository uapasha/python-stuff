# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_auto_20160510_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='job',
            field=models.ForeignKey(verbose_name=b'Job description', to='jobs.Job'),
        ),
    ]
