import sqlite3 #імпорт бібліотеки

print(sqlite3.sqlite_version)
conn = sqlite3.connect('example.db') #викликання методу connect (зв'язок з потрібною БД)
c = conn.cursor() #штука, яка робить те, що нам треба
c.execute('''CREATE TABLE firsttable
                 (Name TEXT,
                  Sex TEXT CHECK(Sex IN ('F', 'M')) NOT NULL DEFAULT 'M',
                  RecordBook  INTEGER,
                  Mark INTEGER,
                  Passed TEXT CHECK(Passed IN ('YES', 'NO')) NOT NULL DEFAULT 'NO')''')
#print(conn)
c.execute('''INSERT INTO firsttable VALUES
             ('Mariia Fedorova', 'F', 12345, 74, 'YES')''')
c.execute('''INSERT INTO firsttable VALUES
             ('Oleh Ivanov', 'M', 12545, 84, 'YES')''')
conn.commit() #збереження результату
for row in c.execute('SELECT * FROM firsttable'): #штука, яка прибирає однакові рядки в таблиці
    print(row) #напр, якщо написати рядки, які вводять дані про людину (х) і 2 рази запустити програму,
               #то в таблицю буде вписано 2 однакові рядки. Завдяки цьому циклу дані про людину (х)
               #потрапляють у таблицю лише ОДИН раз

conn.close() #закриття connect