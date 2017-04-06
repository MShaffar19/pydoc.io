# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-06 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import pydoc.core.conf


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_add-pypi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='file',
            field=models.FileField(blank=True, help_text='the distribution file (if it was mirrord locally)', max_length=5000, null=True, upload_to=pydoc.core.conf.distribution_upload_to),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='filename',
            field=models.CharField(blank=True, default='', help_text='the filename as provided by pypi', max_length=5000),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='url',
            field=models.URLField(blank=True, help_text='the original url provided by pypi', max_length=5000, null=True),
        ),
    ]