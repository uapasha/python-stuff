# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_auto_20160510_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='colleagues',
            field=models.ManyToManyField(to='persons.Person', null=True, related_name='_person_colleagues_+', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='job',
            field=models.ForeignKey(verbose_name='Job description', to='jobs.Job'),
        ),
    ]
