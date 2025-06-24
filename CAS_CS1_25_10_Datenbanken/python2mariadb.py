"""
Created on Jun 18 19:43:24 2023
@author: marr

Interacting with MariaDB
"""
# import of MariaDB Connector
import mariadb
# Setting up the connection to the database
try:
    conn = mariadb.connect(
        user="pythonAppUser",
        password="-w-3-b-007-c0n",
        host="localhost",
        port=3306,
        database="cas cs1 fs25"
    )

    # Getting a cursor.
    # The cursor provides an interface for interacting with the database, such as running SQL queries and managing transactions
    cur = conn.cursor()

except mariadb.Error as e:
    print(f"Error connecting to database: {e}")


# adding a record to the table Mitarbeiter
def add_data(ma_num, first_name, last_name, abt_num):
    try:
        cur.execute("insert into mitarbeiter (manummer, vorname, nachname, abtnummer) values (?, ?, ?, ?)",
                    (ma_num, first_name, last_name, abt_num))
        print("Successfully added entry to database")
        # Committing the transaction
        conn.commit()
    except mariadb.Error as e:
        print(f"Error adding entry to database: {e}")


# retrieving records from the table Mitarbeiter that match a pattern at the attribute Nachname
def get_data(last_name):
    try:
        cur.execute("select manummer, vorname, nachname from mitarbeiter where nachname like ?",
                    ("%" + last_name + "%",))
        for (ma_num, first_name, last_name) in cur:
            print(f"Retrieved: {ma_num}, {first_name}, {last_name}")
    except mariadb.Error as e:
        print(f"Error retrieving entry from database: {e}")

def get_emoOfSameDept(ma_num):
    try:
        #cur.execute(f"CALL getmaderselbenabteilung({ma_num})")
        cur.callproc('getmaderselbenabteilung', [ma_num])
        for (ma_num, first_name, last_name) in cur:
            print(f"Retrieved: {ma_num}, {first_name}, {last_name}")
    except mariadb.Error as e:
        print(f"Error retrieving entry from database: {e}")

# Testing of the different functions (by commenting out one of the following 2 lines)
# add_data(95, "Hans", "Muster", 3)
#get_data("r")

get_emoOfSameDept(3)

# Closing the cursor
cur.close()

# Closing the connection
conn.close()
