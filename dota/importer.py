"""
DotA 2 app
Match data importer
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
    """ Import all matches for given player ID """
    hist = DOTA_API.get_match_history(account_id=pid)
    for match in hist['matches']:
        str_match = match['match_id']
        obj_player = dota.factory.player_get_byid(pid)
        dota.factory.match_put(str_match, obj_player)
    print '--- Finished match import for ' + str(obj_player)


def populate_detail(mid, pid):
    """ Import all details for given match ID """
    details = DOTA_API.get_match_details(match_id=mid.match_id)
    for detail in details['players']:
        player_id = detail['account_id']
        if player_id == pid.player_id:
            item1 = ''
            item2 = ''
            item3 = ''
            item4 = ''
            item5 = ''
            item6 = ''

            if 'item_0_name' in detail:
                item1 = detail['item_0_name']
            if 'item_1_name' in detail:
                item2 = detail['item_1_name']
            if 'item_2_name' in detail:
                item3 = detail['item_2_name']
            if 'item_3_name' in detail:
                item4 = detail['item_3_name']
            if 'item_4_name' in detail:
                item5 = detail['item_4_name']
            if 'item_5_name' in detail:
                item6 = detail['item_5_name']

            detail_array = [detail['hero_name'], detail['level'],
                            detail['kills'], detail['deaths'], detail['assists'],
                            detail['last_hits'], detail['denies'],
                            detail['hero_damage'], detail['tower_damage'],
                            item1, item2, item3, item4, item5, item6,
                            details['game_mode_name']]
            dota.factory.detail_put(mid, pid, detail_array)
    print '--- Finished detail import for match ' + str(mid)


PLAYERS = dota.factory.player_get_allid()
for player in PLAYERS:
    populate_matches(player)
    obj_player_out = dota.factory.player_get_byid(player)
    for obj_match_out in dota.factory.match_get_byplayer(obj_player_out):
        populate_detail(obj_match_out, obj_player_out)
