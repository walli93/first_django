# Generated by Django 2.2.5 on 2019-09-27 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190927_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=20)),
                ('reg_no', models.TextField()),
                ('yom', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='essays',
            name='essay_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 16, 1, 53, 248202), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 16, 1, 53, 160436), verbose_name='date published'),
        ),
    ]
