# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero', models.CharField(max_length=24)),
                ('level', models.IntegerField(default=0)),
                ('kills', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('last_hits', models.IntegerField(default=0)),
                ('denies', models.IntegerField(default=0)),
                ('hero_dmg', models.IntegerField(default=0)),
                ('tower_dmg', models.IntegerField(default=0)),
                ('item1', models.CharField(max_length=36)),
                ('item2', models.CharField(max_length=36)),
                ('item3', models.CharField(max_length=36)),
                ('item4', models.CharField(max_length=36)),
                ('item5', models.CharField(max_length=36)),
                ('item6', models.CharField(max_length=36)),
                ('mode', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player',
            field=models.ForeignKey(to='dota.Player'),
        ),
        migrations.AddField(
            model_name='detail',
            name='match',
            field=models.ForeignKey(to='dota.Match'),
        ),
        migrations.AddField(
            model_name='detail',
            name='player',
            field=models.ForeignKey(to='dota.Player'),
        ),
    ]
