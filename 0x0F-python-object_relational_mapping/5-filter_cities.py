#!/usr/bin/python3
"""_summary_"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("select cities.name from cities\
                inner join states on cities.state_id = states.id \
                and states.name like '{}'\
                ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
