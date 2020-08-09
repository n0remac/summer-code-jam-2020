# Generated by Django 3.1 on 2020-08-09 15:20

import datetime

import django.core.validators
import django.utils.timezone
import page_maker.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('style_sheet', models.FileField(upload_to='styles/')),
                ('thumbnail', models.ImageField(default='thumbnails/placeholder_img.png', editable=False, upload_to='thumbnails/', validators=[django.core.validators.validate_image_file_extension], verbose_name='thumbnail (leave empty-generated automatically)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edit_date', models.DateTimeField(editable=False)),
                ('thumbnail', models.ImageField(default='thumbnails/placeholder_img.png', editable=False, upload_to='thumbnails/', validators=[django.core.validators.validate_image_file_extension], verbose_name='thumbnail (leave empty-generated automatically)')),
                ('thumbnail_edit_date', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0), editable=False)),
                ('user_title', models.CharField(max_length=100, verbose_name='page title')),
                ('user_text_1', models.TextField(blank=True, verbose_name='subtitle paragraph')),
                ('user_text_2', models.TextField(verbose_name='main body paragraph')),
                ('user_text_3', models.TextField(blank=True, verbose_name='closing paragraph')),
                ('user_image_1', models.ImageField(blank=True, max_length=200, null=True, upload_to=page_maker.models.get_user_dir_path, validators=[django.core.validators.validate_image_file_extension], verbose_name='header image')),
                ('user_image_2', models.ImageField(blank=True, max_length=200, null=True, upload_to=page_maker.models.get_user_dir_path, validators=[django.core.validators.validate_image_file_extension], verbose_name='main image')),
                ('user_image_3', models.ImageField(blank=True, max_length=200, null=True, upload_to=page_maker.models.get_user_dir_path, validators=[django.core.validators.validate_image_file_extension], verbose_name='footer image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('template_used', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='page_maker.template')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_datetime', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_maker.webpage')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_maker.webpage')),
            ],
        ),
    ]
