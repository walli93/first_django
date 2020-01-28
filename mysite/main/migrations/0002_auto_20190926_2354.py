# Generated by Django 2.2.5 on 2019-09-26 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essay_title', models.CharField(max_length=200)),
                ('essay_content', models.TextField()),
                ('essay_published', models.DateTimeField(default=datetime.datetime(2019, 9, 26, 23, 54, 24, 561619), verbose_name='date published')),
            ],
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 26, 23, 54, 24, 502139), verbose_name='date published'),
        ),
    ]
