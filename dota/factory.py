import mysql.connector

mysql_cfg = {
  'user': 'pqn',
  'password': 'herpderp',
  'host': '127.0.0.1',
  'database': 'pqn_dota'
}

conn = mysql.connector.connect(**mysql_cfg)
conn.close()

