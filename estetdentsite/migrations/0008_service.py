# Generated by Django 2.0.2 on 2018-05-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetdentsite', '0007_spec_short_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('info', models.TextField()),
                ('price', models.IntegerField(max_length=256)),
            ],
        ),
    ]
