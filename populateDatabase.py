import sqlite3

conn = sqlite3.connect('restaurant.db')
c = conn.cursor()


def insert_branch():
    # c.execute(''' INSERT INTO branch VALUES('b1','brigaderoad',10,4) ''')
    # c.execute('''INSERT
    # INTO
    # branch
    # VALUES('b2', 'koramangala', 4, 3)''')
    # c.execute('''INSERT
    # INTO
    # branch
    # VALUES('b3', 'jayanagar', 6, 5)''')
    c.execute(''' INSERT INTO branch VALUES('b4','indranagar',12,3)''')
    c.execute(''' INSERT INTO branch VALUES('b5','BTM',8,3)''')
    conn.commit()
    conn.close()


def insert_chefs():
    # c.execute(''' INSERT
    # INTO
    # chefs
    # VALUES('c1', 'm1', 'harish', '01 / 04 / 2000', 'b1', 'north_in', 30000)''')

    # c.execute('''INSERT
    # INTO
    # chefs
    # VALUES('c1', 'm2', 'harish', '01 / 04 / 2000', 'b1', 'north_in', 30000)''')
    # c.execute('''
    # INSERT
    # INTO
    # chefs
    # VALUES('c1', 'm3', 'harish', '01 / 04 / 2000', 'b1', 'north_in', 30000);''')
    c.execute('''INSERT INTO chefs VALUES('c2','m4','aman','01/06/2012','b3','italian',40000)''')
    c.execute('''INSERT INTO chefs VALUES('c2','m5','aman','01/06/2012','b3','italian',40000)''')
    c.execute('''INSERT INTO chefs VALUES('c2','m6','aman','01/06/2012','b3','italian',40000)''')
    c.execute('''INSERT INTO chefs VALUES('c3','m7','savani','01/06/2010','b2','chinese',50000)''')
    c.execute('''INSERT INTO chefs VALUES('c4','m8','narayana','01/01/2015','b4','south_indian',40000)''')
    c.execute('''INSERT INTO chefs VALUES('c5','m9','manohar','01/01/2017','b5','deserts',40000)''')
    conn.commit()
    conn.close()


def insert_menu():
    # c.execute('''INSERT INTO menu VALUES('m1','Gobi_Manchurian',200)''')
    # c.execute('''INSERT INTO menu VALUES('m2','Chicken_roll',250)''')
    # c.execute('''INSERT INTO menu VALUES('m3','Mushroom_Manchurian',200)''')
    c.execute('''INSERT INTO menu VALUES('m4','pasta',200)''')
    c.execute('''INSERT INTO menu VALUES('m5','pizza',400)''')
    c.execute('''INSERT INTO menu VALUES('m6','lasaigna',400)''')

    conn.commit()
    conn.close()


def insert_customer():
    c.execute(''' INSERT
        INTO
        customer
        VALUES('1', 'noel', 9999999999, 01, 4,'b1', 2)''')
    c.execute(''' INSERT
        INTO
        customer
        VALUES('2','anagha', 9999999998, 2, 4,'b1', 3);''')

    c.execute(''' INSERT
        INTO
        customer
        VALUES('3', 'gowri', 9999999997, 3, 2,'b1', 6);''')
    conn.commit()
    conn.close()


def insert_orders():
    c.execute('''INSERT INTO orders VALUES('m1','01')''')
    c.execute('''INSERT
INTO
orders
VALUES('m1', '02')''')
    c.execute('''INSERT
INTO
orders
VALUES('m2', '01')''')
    conn.commit()
    conn.close()


def insert_parking():
    c.execute(''' INSERT INTO parking VALUES( 'ma2470',4,'b1','2',1800,2300)''')
    c.execute(''' INSERT
INTO
parking
VALUES( 'ab1234', 2,'b3', '9', 1200, 1700)''')
    c.execute('''INSERT
INTO
parking
VALUES( 'bc5678', 4,'b2', '1', 1300, 1500) ''')
    conn.commit()
    conn.close()


def insert_server():
    # c.execute(''' INSERT INTO server VALUES('s1','01','kiran',9886001211,35000,'b1',3) ''')
    # c.execute('''INSERT
    # INTO
    # server
    # VALUES('1', '02', 'kiran', 9886001211, 35000,'b1', 3) ''')
    # c.execute(''' INSERT
    # INTO
    # server
    # VALUES('s2', '01', 'ajay', 9876006611, 10000,'b2', 5)''')
    c.execute(''' INSERT INTO server VALUES('s2','02','ajay',9876006611,10000,'b2',5) ''')
    c.execute(''' INSERT INTO server VALUES('s3','03','aniket',9876346611,25000,'b1',6) ''')
    c.execute(''' INSERT INTO server VALUES('s3','04','aniket',9876346611,25000,'b1',6) ''')
    c.execute(''' INSERT INTO server VALUES('s4','05','benny',9823612110,20000,'b1',2) ''')
    c.execute(''' INSERT INTO server VALUES('s4','06','benny',9823612110,20000,'b1',2) ''')
    conn.commit()
    conn.close()

