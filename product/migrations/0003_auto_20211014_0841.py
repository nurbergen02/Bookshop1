# Generated by Django 3.2.7 on 2021-10-14 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211014_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='author',
            name='status',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='status',
        ),
    ]
