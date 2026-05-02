import sqlite3

def main():
    
    conn = sqlite3.connect('phonebook.db')

    
    cur = conn.cursor()

    
    add_entries_table(cur)

    
    add_entries(cur)

    
    conn.commit()

    
    display_entries(cur)

    
    conn.close()

def add_entries_table(cur):
    
    cur.execute('DROP TABLE IF EXISTS Entries')

    
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                         Name TEXT,
                                         Phone TEXT)''')


def add_entries(cur):
    phonebook_entries = [
        (1, 'Roe Smith', '503-209-2000'),
        (2, 'Adam Piper', '532-440-0200'),
        (3, 'Peter Peterson', '100-100-1234'),
        (4, 'Michael Jordan', '940-200-7950'),
        (5, 'Stewie Peterson', '707-909-2309')
    ]

    for row in phonebook_entries:
        cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


def display_entries(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')


if __name__ == '__main__':
    main()
