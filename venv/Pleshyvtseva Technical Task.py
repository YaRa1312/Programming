import sqlite3

connection = sqlite3.connect('d.db')
connection = connection.cursor()
connection.execute('''CREATE TABLE dtable
                 (driver_id INTEGER PRIMARY KEY NOT NULL,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  updated_at TEXT NOT NULL
                  )''')
connection.execute('''INSERT INTO dtable VALUES
             (1, 'Iryna', 'Pleshyvtseva', '11/09/2002', '14/12/2021')''')
connection.commit()
for row in connection.execute('SELECT * FROM dtable'):
    print(row)

connection.close()


#def connect_to_db():
 #   connect = sqlite3.connect('database_drivers.db')
  #  return connect

#def create_db_table_1():
 #   try:
  #      connect = connect_to_db()
   #     connect.execute('''
    #        CREATE TABLE Drivers (
     #           driver_id INTEGER PRIMARY KEY NOT NULL,
      #          first_name TEXT NOT NULL,
       #         last_name TEXT NOT NULL,
        #        created_at TEXT NOT NULL,
         #       updated_at TEXT NOT NULL
          #  );
        #''')

        #connect.commit()
        #print("Driver table created successfully")
    #except:
     #   print("Driver table creation failed - Maybe table")
    #finally:
      #  connect.close()

#def insert_driver(driver):
 #   inserted_driver = {}
  #  try:
    #    connection = connect_to_db()
   #     cursor = connection.cursor()
     #   cursor.execute("INSERT INTO Drivers (first_name, last_name, created_at, updated_at) VALUES (?, ?, ?, ?)", (driver['first_name'],
      #                driver['last_name'], driver['created_at'], driver['updated_at']
       #               ) )
       # connection.commit()
        #inserted_driver = get_driver_by_id(cur.lastrowid)
    #except:
     #   connection().rollback()

    #finally:
     #   connection.close()

    #return inserted_driver
