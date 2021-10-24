import sqlite3

conn = sqlite3.connect('sampledb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tests')

cur.execute('CREATE TABLE Tests (email TEXT, name TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    domain = email.split('@')
    name = domain[0]
    address = domain[1]

    cur.execute('SELECT count FROM Tests WHERE email = ?', (address,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Tests (email, name, count)
        VALUES (?,?,1)''', (address, name))
    else:
        cur.execute(
            'UPDATE Tests SET count = count + 1 WHERE email = ?', (address,))
    conn.commit()

sqlstr = 'SELECT email, name, count FROM Tests ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1], row[2])

cur.close()
