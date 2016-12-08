# use ET to parth XML
import xml.etree.cElementTree as ET
# and sqlite3 to talk to database
import sqlite3

conn = sqlite3.connect("trackdb.sqlite")
# establish a connection to trackdb.sqlite file on disk
cur = conn.cursor()
# cursor is the way we actually send the commands

# we can also use different technique: CREATE TABLE IF NOT EXISTS (...)
# so we don't have to DROP before
cur.executescript('''   DROP TABLE IF EXISTS Artist;
                        DROP TABLE IF EXISTS Album;
                        DROP TABLE IF EXISTS Track;

                        CREATE TABLE Artist
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);

                        CREATE TABLE Album
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE,
                             artist_id INTEGER);

                        CREATE TABLE Track
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE,
                             len INTEGER, rating INTEGER, count INTEGER,
                             album_id INTEGER);
                        ''')

fname = raw_input("Enter file name: ")
if len(fname)<1 : fname = "Library.xml"


def lookup (d, key_text):
    found = False
#
    for child in d:
        # equal to:       if found = True: return child.text
        if found: return child.text
        if child.tag == "key" and child.text == key_text: found = True
# that function looping throught all tags within dictionary entry = d
# such as <key></key><integer></integer><string></string><data></data>
# Loop through looking for key tagName, and then I go to the next tag and I return the text for that

    return None
#   if nothing found will return NULL

stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict")
# A dictionary within a dictionary within a dictionary, like go down the tree
# <all> it is all dictionary = all track dictionary, len(all) = how many dictionaries we have
print "Dict count:", len(all)
# <entry> is the XML object that represents a DICT object, or one of dictionaries which contains information about the track
for entry in all:
    if (lookup(entry, "Track ID") is None) : continue
    # we skip dictionary with empty track name

    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play count")
    rating = lookup(entry, "Rating")
    lenght = lookup(entry, "Total Time")

    if name is None or artist is None or album is None: continue
    # we skip dictionaty with any of that variables empty

    print "Name:",name,"--  Artist:", artist,"-- Album:", album,"--  Play count:", count,"--  Rating:", rating,"--  Total Time:", lenght

    # INSERT and of if something goes wrong IGNORE, so INSERT OR IGNORE (ignore it if it's already there)
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist, ))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ?)", (album, artist_id))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album, ))
    album_id = cur.fetchone()[0]

    # we can do it in a different way (to avoid duplicates):
    # We could do a SELECT. We could check if it's already there: We could do an INSERT if it wasn't there and an UPDATE if it was there
    cur.execute("INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) VALUES (?, ?, ?, ?, ?)", (name, album_id,lenght, rating,count))

    conn.commit()



