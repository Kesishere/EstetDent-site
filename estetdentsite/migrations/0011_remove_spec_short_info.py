# Generated by Django 2.0.2 on 2018-05-16 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estetdentsite', '0010_spec_spec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spec',
            name='short_info',
        ),
    ]
