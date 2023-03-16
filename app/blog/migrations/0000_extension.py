from __future__ import unicode_literals

from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    run_before = [
        ('blog', '0001_initial'),  # noqa: BLK100
    ]

    operations = [
        TrigramExtension(),
    ]
