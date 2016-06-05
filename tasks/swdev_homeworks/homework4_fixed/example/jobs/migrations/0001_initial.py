# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name=b'job description')),
            ],
        ),
    ]
