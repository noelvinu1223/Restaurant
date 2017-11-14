import sqlite3
import os

conn = sqlite3.connect('../PycharmProjects/Restaurant/restaurant.db')
cursor = conn.execute('''SELECT * FROM server''')
b = ["s_id", "table_no", "s_name", "phone", "salary", "b_id", "absent"]
list7 = []
for list8 in cursor:
    list7.append(dict(zip(b, list8)))
conn.close()
print(list7)
