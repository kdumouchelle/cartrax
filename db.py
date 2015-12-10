__author__ = 'Kyle Dumouchelle'
# CPSC409 final, 12/09/2015

import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    # get cursor for SQL execution
    c = connection.cursor()

    # create table
    c.execute("DROP TABLE IF EXISTS items")
    c.execute("""CREATE TABLE items(item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    maintenance_type TEXT NOT NULL, date TEXT NOT NULL, odometer INTEGER NOT NULL,
    status INTEGER NOT NULL)""")

    # insert dummy data
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Tires","12/25/2014", 10000, 1)""")
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Brakes","12/09/2015", 15000, 1)""")
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Brakes","12/10/2015", 15001, 1)""")
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Headlights","02/28/1890", 10, 1)""")
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Air Filter","06/01/2018", 200000, 1)""")
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Coolant","07/28/1993", 5093, 1)""")
    c.execute("""INSERT INTO items ( maintenance_type, date, odometer, status)
              VALUES("Brakes","01/01/1889", 0, 1)""")