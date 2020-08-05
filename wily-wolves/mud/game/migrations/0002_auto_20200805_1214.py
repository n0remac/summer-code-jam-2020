# Generated by Django 3.0.8 on 2020-08-05 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coord', models.BigIntegerField(default=0)),
                ('y_coord', models.BigIntegerField(default=0)),
                ('z_coord', models.BigIntegerField(default=0)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('max_health', models.BigIntegerField(default=100)),
                ('current_health', models.BigIntegerField(default=100)),
                ('npc_type', models.CharField(choices=[('MC', 'Merchant'), ('EN', 'Enemy'), ('CV', 'Civilian')], default='EN', max_length=2)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Location')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='location_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.Location'),
        ),
    ]
