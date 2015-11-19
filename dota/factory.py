from models import Player
from models import Match
from models import Detail


def player_check(pid):
    return Player.objects.filter(player_id=pid).exists()


def player_put(pid, name):
    if not player_check(pid):
        q = Player(player_id=pid, name=name)
        q.save()


def player_get_byid(pid):
    return Player.objects.get(player_id=pid)


def player_get_byname(name):
    return Player.objects.get(name=name)


def player_get_allid():
    return Player.objects.values_list('player_id', flat=True)


def player_get_all():
    return Player.objects.all()


def match_check(mid, pid):
    return Match.objects.filter(match_id=mid, player=pid).exists()


def match_put(mid, pid):
    if not match_check(mid, pid):
        q = Match(match_id=mid, player=pid)
        q.save()
        return True
    return False


def match_get_byid(mid):
    return Match.objects.get(match_id=mid)


def match_get_byplayer(pid):
    return Match.objects.filter(player=pid)


def match_get_all():
    return Match.objects.all()


def detail_check(mid, pid):
    return Detail.objects.filter(match=mid, player=pid).exists()


def detail_put(mid, pid,
               hero, lvl,
               k, d, a,
               lh, dn,
               hd, td,
               i1, i2, i3, i4, i5, i6,
               mode):
    if not detail_check(mid, pid):
        q = Detail(match=mid, player=pid,
                   hero=hero, level=lvl,
                   kills=k, deaths=d, assists=a,
                   last_hits=lh, denies=dn,
                   hero_dmg=hd, tower_dmg=td,
                   item1=i1, item2=i2, item3=i3, item4=i4, item5=i5, item6=i6,
                   mode=mode)
        q.save()


def detail_get_byplayer(pid):
    return Detail.objects.filter(player=pid)


# def noob_get():
