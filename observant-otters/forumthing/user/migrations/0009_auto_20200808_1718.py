# Generated by Django 3.0.8 on 2020-08-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200808_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='nickname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
