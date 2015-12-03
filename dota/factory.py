"""
Data factory
"""
from models import Player, Match, Detail


def player_check(pid):
    """ Check if specified player exists """
    return Player.objects.filter(player_id=pid).exists()


def player_put(pid, name):
    """ Insert player via DotA2 ID """
    if not player_check(pid):
        query = Player(player_id=pid, name=name)
        query.save()
        return True
    return False


def player_get_byid(pid):
    """ Retrieve player object by DotA2 ID """
    return Player.objects.get(player_id=pid)


def player_get_byname(name):
    """ Retrieve player object by name """
    return Player.objects.get(name=name)


def player_get_allid():
    """ Return a list of all player IDs (as strings) in DB """
    return Player.objects.values_list('player_id', flat=True)


def player_get_all():
    """ Return all player objects """
    return Player.objects.all()


def match_check(mid, pid):
    """ Check if specified match/player pair exists """
    return Match.objects.filter(match_id=mid, player=pid).exists()


def match_put(mid, pid):
    """ Insert match via Match ID and DotA2 ID """
    if not match_check(mid, pid):
        query = Match(match_id=mid, player=pid)
        query.save()
        return True
    return False


def match_get_byid(mid):
    """ Return match object via Match ID """
    return Match.objects.get(match_id=mid)


def match_get_byplayer(pid):
    """ Return list of match objects via DotA2 ID """
    return Match.objects.filter(player=pid)


def match_get_byplayer_byid(mid, pid):
    """ Return single match/player object via DotA2 ID and Match ID """
    return Match.objects.filter(match_id=mid, player=pid)


def match_get_all():
    """ Return all match objects """
    return Match.objects.all()


def detail_check(mid, pid):
    """ Check if specified match/player pair detail exists """
    return Detail.objects.filter(match=mid, player=pid).exists()


def detail_put(obj_match, obj_player, details):
    """ Insert match details via Match and DotA2 ID """
    if not detail_check(obj_match, obj_player):
        query = Detail(match=obj_match, player=obj_player,
                       hero=details[0], level=details[1],
                       kills=details[2], deaths=details[3], assists=details[4],
                       last_hits=details[5], denies=details[6],
                       hero_dmg=details[7], tower_dmg=details[8],
                       item1=details[9], item2=details[10], item3=details[11],
                       item4=details[12], item5=details[13], item6=details[14],
                       mode=details[15])
        query.save()
        return True
    return False


def detail_get_byplayer(pid):
    """ Return list of detail objects via DotA2 ID """
    return Detail.objects.filter(player=pid)


def noob_get_week():
    """ Return player/match with the most deaths within the week """

def noob_get_month():
    """ Return player/match with the most deaths within the month """
