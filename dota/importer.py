import os
import django
import dota.factory
import dota2api

os.environ['DJANGO_SETTINGS_MODULE'] = 'dota.settings'
django.setup()

API_KEY = 'CC538567909A04C219251543B4556442'
api = dota2api.Initialise(API_KEY)


def populate_matches(pid):
    hist = api.get_match_history(account_id=pid)
    for match in hist['matches']:
        m = match['match_id']
        p = dota.factory.player_get_byid(pid)
        dota.factory.match_put(m, p)
    print '--- Finished match import for ' + str(p)


def populate_detail(mid, pid):
    details = api.get_match_details(match_id=mid)
    for detail in details['players']:
        player = detail['account_id']
        if player == pid:
            p = dota.factory.player_get_byid(player)
            m = dota.factory.match_get_byid(mid)
            dota.factory.detail_put(m, p,
                                    detail['hero_name'],
                                    detail['level'],
                                    detail['kills'],
                                    detail['deaths'],
                                    detail['assists'],
                                    detail['last_hits'],
                                    detail['denies'],
                                    detail['hero_damage'],
                                    detail['tower_damage'],
                                    detail['item_0_name'],
                                    detail['item_1_name'],
                                    detail['item_2_name'],
                                    detail['item_3_name'],
                                    detail['item_4_name'],
                                    detail['item_5_name'],
                                    details['game_mode_name'])
    print '--- Finished detail import for match ' + str(mid)


players = dota.factory.player_get_allid()
for player in players:
    populate_matches(player)
    # p = dota.factory.player_get_byid(player)
    # for m in dota.factory.match_get_byplayer(p):
    #     populate_detail(m, player)
