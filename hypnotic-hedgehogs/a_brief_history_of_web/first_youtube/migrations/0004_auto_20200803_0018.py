# Generated by Django 3.0.8 on 2020-08-02 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_youtube', '0003_comment_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('publisher', models.CharField(max_length=30)),
                ('view_count', models.IntegerField(default=0)),
                ('now_playing', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 0, 18, 48, 52808)),
        ),
    ]
