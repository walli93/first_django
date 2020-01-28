# Generated by Django 2.2.5 on 2019-09-27 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190927_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('age', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='essays',
            name='essay_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 15, 39, 8, 89324), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 15, 39, 8, 21551), verbose_name='date published'),
        ),
    ]