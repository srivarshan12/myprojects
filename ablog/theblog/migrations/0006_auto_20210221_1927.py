# Generated by Django 3.1.3 on 2021-02-21 13:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
