# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_remove_status_recompensa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
