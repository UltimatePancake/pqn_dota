from dota.models import Player
from dota.models import Match
from dota.models import Detail
import mysql.connector

mysql_cfg = {
  'user': 'pqn',
  'password': 'herpderp',
  'host': '127.0.0.1',
  'database': 'pqn_dota'
}

def player_check(pid):
  query = ('SELECT (1) FROM Player WHERE player_id = %s')
  params = (pid)
  conn = mysql.connector.connect(**mysql_cfg)

  conn.execute(query, params)

  if conn.fetchone()[0]:
    conn.close()
    return True

  conn.close()
  return False
  
def player_put(pid, name):
  query = ('INSERT INTO Player (player_id, name) VALUES (%s, %s)')
  params = (pid, name)
  conn = mysql.connector.connect(**mysql_cfg)

  if not self.player_check(pid):
    conn.execute(query, params)
    conn.commit()

  conn.close()

def player_get_byid(pid):
  query = ('SELECT (1) FROM Player WHERE player_id = %s')
  params = (pid)
  conn = mysql.connector.connect(**mysql_cfg)

  conn.execute(query, params)

  # TODO: Proper return

  conn.close()

def player_get_byname(name):
  query = ('SELECT (1) FROM Player WHERE name = %s')
  params = (name)
  conn = mysql.connector.connect(**mysql_cfg)

  conn.execute(query, params)

  # TODO: Proper return

  conn.close()

def match_check(mid, pid):
  query = ('SELECT (1) FROM Match WHERE match_id = %s AND player = %s')
  params = (mid, pid)
  conn = mysql.connector.connect(**mysql_cfg)

  conn.execute(query, params)
  if conn.fetchone()[0]:
    conn.close()
    return True

  conn.close()
  return False

def match_put(mid, pid):
  # TODO: Proper insert


def detail_check(mid, pid):
  query = ('SELECT (1) FROM Detail WHERE match = %s AND player = %s')
  params = (mid, pid)
  conn = mysql.connector.connect(**mysql_cfg)

  conn.execute(query, params)
  if conn.fetchone()[0]:
    conn.close()
    return True

  conn.close()
  return False

def detail_put(mid, pid, hero, lvl, k, d, a, lh, dn, hd, td, i1, i2, i3, i4, i5, i6, mode):
  # TODO Proper insert

def noob_get:
  query = ('SELECT match, player, hero, kills, deaths, assists FROM Detail WHERE HAVING MAX(deaths - kills)')
  conn = mysql.connector.connect(**mysql_cfg)

  conn.execute(query)

  # TODO: Proper return

  conn.close()