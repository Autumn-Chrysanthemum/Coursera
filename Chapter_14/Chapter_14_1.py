#impotr libraty which we will use to talk to database
import sqlite3

# we're going to use a database in this application and
# we're going to store that database in the file emaildb.sqllite
# it's creating a connection object
# and the connection object make a connection to a file
conn = sqlite3.connect("emaildb.sqlite")
# the command or the row that's coming back = cursors
# cur variable has a cursor object in it
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
# triple-quoted string if the line is broken we can use to see it
cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

fname = raw_input("Enter file name: \n")
if (len(fname)<1): fname = "mbox-short.txt"
#fname = "mbox-short.txt"

fh = open(fname)
# So at the end of the day we're going to have a table that's the name and the count.
# Name, count, name, count, name, count. So that's what this loop does.
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    print email
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email, ))
    # The question mark is a place holder to be filled in and so that says this is going to be something
    # (email, ) is tuple. Shoud be with comma. The first thing in the tuple is what will be substituted for the question mark
    # the cursor now has done a SELECT, that has what's called a row set.
    # And that's all the rows that would have met that. Including potentially no rows whatever
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email, ))
    else:
        cur.execute("UPDATE Counts SET count=count+1 WHERE email = ?", (email, ))

    # This statement commit outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes

    conn.commit()
#  And so commit basically says, if you've been doing stuff in memory, dear SQLite, please write it back to disk

# https://www.sqlite.org/lang_select.html
sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

print
print "Counts:"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
