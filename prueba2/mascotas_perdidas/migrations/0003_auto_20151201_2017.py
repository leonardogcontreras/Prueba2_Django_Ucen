# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas_perdidas', '0002_auto_20151201_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascotas_perdidas',
            old_name='status',
            new_name='extraviado',
        ),
    ]
