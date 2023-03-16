# Generated by Django 4.1.7 on 2023-03-02 13:49

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),  # noqa: BLK100
        ('blog', '0003_comment_comment_blog_commen_created_0e6ed4_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags',
            ),
        ),
    ]
