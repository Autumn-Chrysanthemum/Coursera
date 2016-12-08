import sqlite3

conn = sqlite3.connect("music.sqlite3")
# The connect operation makes a connection to the database
# stored in the file music.sqlite3 in the current directory
# In our simple examples the database will just be a local file
# in the same directory as the Python code we are running.
# sometimes the database is stored on a separate database server


cur = conn.cursor()
# A cursor is like a file handle that we can use to perform operations
# on the data stored in the database. Similar to open()

cur.execute("DROP TABLE IF EXISTS Tracks")
cur.execute("CREATE TABLE Tracks (title TEXT, plays INTEGER)")

cur.execute("INSERT INTO Tracks (title, plays) VALUES (?,?)",("Thundrtstruck", 20))
cur.execute("INSERT INTO Tracks (title, plays) VALUES (?,?)",("My Way",15))
conn.commit()
# use commit() to force the data to be written to the database file


print "\nTracks:"

# After we execute the SELECT statement,
# the cursor is something we can loop through in a for statement
cur.execute("SELECT title, plays FROM Tracks")
for row in cur:
    print row

# cur.execute("DELETE FROM Tracks WHERE plays < 17")
# conn.commit()
#
# print "\nNew Tracks:"
# cur.execute("SELECT title, plays FROM Tracks")
# for row in cur:
#     print row


conn.close()