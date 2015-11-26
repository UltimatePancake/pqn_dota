"""
Models file for database structure
"""
from django.db import models


# Create your models here.
# PLAYERS
class Player(models.Model):
    """
    Players table
    """
    player_id = models.IntegerField(default=0)
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


# MATCH HISTORY HEAD
class Match(models.Model):
    """
    Matches table
    """
    match_id = models.IntegerField(default=0)
    player = models.ForeignKey(Player)

    def __int__(self):
        return self.match_id


# MATCH HISTORY DETAIL
class Detail(models.Model):
    """
    Match details table
    """
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    hero = models.CharField(max_length=24)
    level = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    last_hits = models.IntegerField(default=0)
    denies = models.IntegerField(default=0)
    hero_dmg = models.IntegerField(default=0)
    tower_dmg = models.IntegerField(default=0)
    item1 = models.CharField(max_length=36, default='')
    item2 = models.CharField(max_length=36, default='')
    item3 = models.CharField(max_length=36, default='')
    item4 = models.CharField(max_length=36, default='')
    item5 = models.CharField(max_length=36, default='')
    item6 = models.CharField(max_length=36, default='')
    mode = models.CharField(max_length=36)

    def __int__(self):
        return str(self.match)
