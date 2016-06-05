# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160507_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='code',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
