# Generated by Django 2.0.2 on 2018-03-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetdentsite', '0006_auto_20180321_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='short_info',
            field=models.TextField(default='test'),
        ),
    ]
