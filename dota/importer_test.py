"""
Importer print test
"""
import os
import django
import dota.factory
import dota2api

os.environ['DJANGO_SETTINGS_MODULE'] = 'dota.settings'
django.setup()

API_KEY = 'CC538567909A04C219251543B4556442'
DOTA_API = dota2api.Initialise(API_KEY)


def populate_matches(pid):
    """ Print all matches for given player ID """
    hist = DOTA_API.get_match_history(account_id=pid)
    for match in hist['matches']:
        str_match = match['match_id']
        obj_player = dota.factory.player_get_byid(pid)
        print 'p = ' + str(obj_player) + ', m = ' + str(str_match)
    print '--- Finished match import for ' + str(obj_player)


def populate_detail(mid, pid):
    """ Print all details for given match ID """
    details = DOTA_API.get_match_details(match_id=mid)
    for detail in details['players']:
        player_id = detail['account_id']
        if player_id == pid:
            print detail['hero_name']
            print detail['level']
            print detail['kills']
            print detail['deaths']
            print detail['assists']
            print detail['last_hits']
            print detail['denies']
            print detail['hero_damage']
            print detail['tower_damage']
            if 'item_0_name' in detail:
                print detail['item_0_name']
            if 'item_1_name' in detail:
                print detail['item_1_name']
            if 'item_2_name' in detail:
                print detail['item_2_name']
            if 'item_3_name' in detail:
                print detail['item_3_name']
            if 'item_4_name' in detail:
                print detail['item_4_name']
            if 'item_5_name' in detail:
                print detail['item_5_name']
            print details['game_mode_name']
    print '--- Finished detail import for match ' + str(mid)


PLAYERS = dota.factory.player_get_allid()
for player in PLAYERS:
    populate_matches(player)
    p = dota.factory.player_get_byid(player)
    for m in dota.factory.match_get_byplayer(p):
        populate_detail(m.match_id, player)
