# Generated by Django 2.0.13 on 2019-04-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basesite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(choices=[('head', 'Код внутри <head>'), ('body_bottom', 'Код перед закрывающим тегом <body>'), ('sidebar_left', 'Баннер в левом сайдбаре'), ('sidebar_right', 'Баннер в правом сайдбаре'), ('footer', 'Баннер в футере')], default='body_bottom', max_length=40, verbose_name='Расположение')),
                ('content', models.TextField(default='Здесь могла быть ваша реклама...', verbose_name='Вставьте сюда содержимое баннера')),
            ],
        ),
    ]
