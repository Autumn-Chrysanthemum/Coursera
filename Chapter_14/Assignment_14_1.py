import sqlite3

conn = sqlite3.connect("Assignment.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = raw_input("Enter file name: \n")
if len(fname)<1: fname = "mbox.txt"

fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    org = pieces[1].split("@")[1]
    # print org
    cur.execute("SELECT count FROM Counts WHERE org = ?", (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org, ))
    else:
        cur.execute("UPDATE Counts SET count=count+1 WHERE org = ?", (org, ))
    conn.commit()

print "Counts:\n"
for row in cur.execute("SELECT org, count FROM Counts ORDER BY count DESC"):
    print row[0], row[1]