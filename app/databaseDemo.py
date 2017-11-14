import sqlite3

conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

# BRANCH
def branch():
    c.execute('''CREATE TABLE branch
    (branch_id VARCHAR(10) PRIMARY KEY ,
     branch_name VARCHAR (10),
     no_of_table NUMERIC(2),
      rating NUMERIC(2))''')

# CHEFS
def chefs():
    c.execute('''CREATE TABLE chefs (
    chef_id VARCHAR(10) ,
    menu_id VARCHAR(10),
    chefs_name VARCHAR(10),
    doj DATE,
    b_id VARCHAR(10),
    speciality VARCHAR(15),
     salary NUMERIC(8),
      PRIMARY KEY(chef_id,menu_id) ,
      FOREIGN KEY(b_id) REFERENCES branch(branch_id) ON DELETE CASCADE)''')

# MENU
def  menu():
    c.execute('''CREATE TABLE menu ( menu_id VARCHAR(10) PRIMARY KEY,
     name VARCHAR(15) ,
     price NUMERIC(4))''')

# SERVERS
def servers():
    c.execute('''CREATE TABLE server (s_id VARCHAR(10) ,
    table_no NUMERIC(2),
     s_name VARCHAR(15) ,
      phone NUMERIC(10),
       salary NUMERIC(8),
        b_id VARCHAR(10) ,
        absent NUMERIC (2),
        PRIMARY KEY(s_id, table_no),
      FOREIGN KEY(b_id ) REFERENCES branch(branch_id) ON DELETE CASCADE)''')

# CUSTOMER
def customer():
    c.execute('''CREATE TABLE customer (cust_id VARCHAR(10) PRIMARY KEY,
    c_name VARCHAR(15),
    phone NUMERIC(10),
    table_no NUMERIC(2),
    no_of_seats NUMERIC(2),
    b_id VARCHAR(10),
    duration NUMERIC(1),
     FOREIGN KEY(b_id) REERENCES branch(branch_id) ON DELETE CASCADE,
      FOREIGN KEY(table_no) FREFERENCES server(table_no) ON DELETE CASCADE)''')

# ORDERS
def orders():
    c.execute('''CREATE TABLE orders( menu_id VARCHAR(10),
    cust_id VARCHAR(10), PRIMARY KEY(menu_id,cust_id) ,
    FOREIGN KEY(menu_id) REFERENCES menu(menu_id) ON DELETE CASCADE,
     FOREIGN KEY(cust_id) REFERENCES customer(cust_id) ON DELETE CASCADE)''')

# PARKING
def parking():
    c.execute('''CREATE TABLE parking( vehicle_no NUMERIC(4) PRIMARY KEY,
     type NUMERIC(1),
     b_id VARCHAR(10) ,
     cust_id VARCHAR(10),
     time_in NUMERIC(2),
     time_out NUMERIC(2),
     FOREIGN KEY(b_id) REFERENCES branch(branch_id) ON DELETE CASCADE,
     FOREIGN KEY(cust_id) REFERENCES customer(cust_id) ON DELETE CASCADE)''')

# FEEDBACK
def feedback():
    c.execute(''' CREATE TABLE feedback(name VARCHAR(20) PRIMARY KEY,
     comments VARCHAR(250),
     food VARCHAR(3),
     service VARCHAR(3))''')

#CUSTOMER_LOG
def customer_log():
    c.execute('''CREATE  TABLE CUSTOMER_LOG ( CUS_NAME VARCHAR(10), date_time DATETIME)''')


conn.close()
