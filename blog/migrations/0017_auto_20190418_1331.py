# Generated by Django 2.0.13 on 2019-04-18 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_top'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='seo_description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='h1',
            new_name='seo_h1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='keywords',
            new_name='seo_keywords',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='seo_title',
        ),
    ]
