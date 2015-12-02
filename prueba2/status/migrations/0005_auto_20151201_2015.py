# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20151201_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(default=1, max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
