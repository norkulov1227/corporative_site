# Generated by Django 4.2.7 on 2024-04-29 03:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_merge_0002_blog_0002_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
