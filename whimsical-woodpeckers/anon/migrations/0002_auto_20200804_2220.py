# Generated by Django 3.0.8 on 2020-08-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='anonuser',
            name='password',
            field=models.CharField(default='abcde', max_length=5),
        ),
    ]