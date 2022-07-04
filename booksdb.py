import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
(title VARCHAR(20) PRIMARY KEY,
author VARCHAR(20),
year INT)''')

curs.execute('INSERT INTO books VALUES("The Weirdstone of Brisingamen", "Alan Garner", 1960)')
curs.execute('INSERT INTO books VALUES("Perdido Street Station", "China Miéville", 2000)')
curs.execute('INSERT INTO books VALUES("Thud!", "Terry Pratchett", 2005)')
curs.execute('INSERT INTO books VALUES("The Spellman Files", "Lisa Lutz", 2007)')
curs.execute('INSERT INTO books VALUES("Small Gods", "Terry Pratchett", 1992)')

curs.close()
