# Generated by Django 2.0.2 on 2018-05-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetdentsite', '0009_auto_20180515_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='spec',
            field=models.CharField(default=123, max_length=256),
            preserve_default=False,
        ),
    ]