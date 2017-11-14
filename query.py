import sqlite3
import os


def sqlite_connection():
    print(os.getcwd())

    conn = sqlite3.connect('../PycharmProjects/Restaurant/restaurant.db')
    return conn


def allbranch():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM branch''')
    b = ["branch_id", "branch_name", "no_of_table", "rating"]
    list2 = []
    for list1 in cursor:
        list2.append(dict(zip(b, list1)))
    conn.close()
    return list2


def allchefs():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM chefs''')
    b = ["chef_id", "menu_id", "chefs_name", "doj", "b_id", "speciality", "salary"]
    list3 = []
    for list4 in cursor:
        list3.append(dict(zip(b, list4)))
    conn.close()
    return list3


def allmenu():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM menu''')
    b = ["menu_id", "name", "price"]
    list5 = []
    for list6 in cursor:
        list5.append(dict(zip(b, list6)))
    conn.close()
    return list5


def allservers():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM server''')
    b = ["s_id", "table_no", "s_name", "phone", "salary", "b_id", "absent"]
    list7 = []
    for list8 in cursor:
        list7.append(dict(zip(b, list8)))
    conn.close()
    return list7


def ci():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM customer''')
    b = ["cust_id", "c_name", "phone", "table_no", "no_of_seats", "b_id", "duration"]
    list9 = []
    for list10 in cursor:
        list9.append(dict(zip(b, list10)))
    conn.close()
    return list9


def fi():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM feedback''')
    b = ["name", "comments", "food", "service"]
    list11 = []
    for list12 in cursor:
        list11.append(dict(zip(b, list12)))
    conn.close()
    return list11


def oi():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM orders''')
    b = ["menu_id", "cust_id"]
    list13 = []
    for list14 in cursor:
        list13.append(dict(zip(b, list14)))
    conn.close()
    return list13


def pi():
    conn = sqlite_connection()
    cursor = conn.execute('''SELECT * FROM parking''')
    b = ["vehicle_no", "type", "b_id", "cust_id", "time_in", "time_out"]
    list15 = []
    for list16 in cursor:
        list15.append(dict(zip(b, list16)))
    conn.close()
    return list15


def q1():
    print(os.getcwd())
    conn = sqlite_connection()
    conn.execute('''CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM parking WHERE type=2''')
    conn.execute('''CREATE VIEW IF NOT EXISTS v2 AS SELECT * FROM parking WHERE type=4''')
    cursor = conn.execute('''SELECT * FROM v1''').fetchall()
    cursor1 = conn.execute('''SELECT * FROM v2''').fetchall()

    conn.close()
    return cursor, cursor1


def q2():
    print(os.getcwd())
    conn = sqlite_connection()

    cursor = conn.execute('''SELECT DISTINCT
      (s.salary),
      s.s_name
      FROM server s, chefs ch 
      WHERE s.salary > ch.salary''').fetchall()

    conn.close()
    return cursor


def q3():
    print(os.getcwd())
    conn = sqlite_connection()

    cursor = conn.execute(
        '''SELECT b.branch_name FROM branch b, customer c WHERE c.c_name='noel' AND c.b_id=b.branch_id AND b.rating>3 ''').fetchall()

    conn.close()
    return cursor


def q4():
    print(os.getcwd())
    conn = sqlite_connection()

    cursor = conn.execute(
        '''SELECT DISTINCT
     (c.chefs_name),
     c.salary
     FROM chefs c, branch b
     WHERE c.b_id = b.branch_id
     AND rating >= 4''').fetchall()

    conn.close()
    return cursor


def q5():
    print(os.getcwd())
    conn = sqlite_connection()

    cursor = conn.execute(
        '''SELECT DISTINCT (s.s_name)
     FROM server s, menu m, orders o, customer c
     WHERE c.cust_id = o.cust_id
      AND c.table_no = s.table_no
      AND o.menu_id = 'm1'
      AND s.b_id = c.b_id''').fetchall()

    conn.close()
    return cursor


def q6():
    print(os.getcwd())
    conn = sqlite_connection()

    cursor = conn.execute(
        ''' SELECT DISTINCT
     (branch_name),
     no_of_table,
     rating
     FROM branch b, chefs ch
     WHERE chefs_name = 'harish'
     AND b.branch_id = ch.b_id''').fetchall()

    conn.close()
    return cursor


def q7():
    print(os.getcwd())
    conn = sqlite_connection()

    cursor = conn.execute(
        ''' SELECT DISTINCT (s_name), salary - 50 FROM server
            WHERE absent>4 ''').fetchall()

    conn.close()
    return cursor


def q8():
    print(os.getcwd())
    conn = sqlite_connection()
    conn.execute('''
        CREATE VIEW IF NOT EXISTS v5 AS
        SELECT
           c.c_name,
           c.phone,
           p.vehicle_no
        FROM parking p, customer c
        WHERE (p.time_out - p.time_in) > 4
        AND p.cust_id = c.cust_id''')
    cursor = conn.execute('''SELECT * FROM v5''').fetchall()

    conn.close()
    return cursor


def q9():
    print(os.getcwd())
    conn = sqlite_connection()
    cursor = conn.execute('''
               SELECT count(c.c_name)
               FROM customer c, menu m, chefs ch, orders o
               WHERE c.cust_id = o.cust_id
               AND o.menu_id = m.menu_id
               AND m.menu_id = ch.menu_id
               AND ch.speciality = 'italian' ''').fetchall()

    conn.close()
    return cursor


def q10():
    print(os.getcwd())
    conn = sqlite_connection()
    conn.execute('''
        CREATE VIEW IF NOT EXISTS v6
        AS
         SELECT sum(price)
         FROM menu m, customer c, orders o
         WHERE o.cust_id = c.cust_id
          AND m.menu_id = o.menu_id''')
    cursor = conn.execute('''SELECT * FROM v6''').fetchall()

    conn.close()
    return cursor


def q11():
    print(os.getcwd())
    conn = sqlite_connection()
    cursor = conn.execute('''
        SELECT
           DISTINCT (ch.chef_id),
                            ch.chefs_name
         FROM chefs ch, orders o
         WHERE ch.menu_id = o.menu_id GROUP BY cust_id HAVING count(cust_id) > 2''').fetchall()

    conn.close()
    return cursor

def trigger():
    conn=sqlite_connection()
    conn.execute('''CREATE  TRIGGER IF NOT EXISTS customer_trigger AFTER INSERT ON customer 
      BEGIN 
         INSERT INTO CUSTOMER_LOG (CUS_NAME, date_time) VALUES (new.c_name, datetime('now'));
       END;
       ''')
    conn.commit()
    conn.close()

