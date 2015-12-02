# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_mp', '0002_info_mp_mascota_perdida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_mp',
            name='mascota_perdida',
            field=models.ForeignKey(to='mascotas_perdidas.Mascotas_Perdidas', null=True),
        ),
    ]
