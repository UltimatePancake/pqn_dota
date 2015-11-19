from django.db import models

# Create your models here.
# PLAYERS
class Player(models.Model):
  player_id = models.IntegerField(default=0)
  name = models.CharField(max_length=16)

# MATCH HISTORY HEAD
class Match(models.Model):
  match_id = models.IntegerField(default=0)
  player = models.ForeignKey(Player)

# MATCH HISTORY DETAIL
class Detail(models.Model):
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
  item1 = models.CharField(max_length=36)
  item2 = models.CharField(max_length=36)
  item3 = models.CharField(max_length=36)
  item4 = models.CharField(max_length=36)
  item5 = models.CharField(max_length=36)
  item6 = models.CharField(max_length=36)
  mode = models.CharField(max_length=36)