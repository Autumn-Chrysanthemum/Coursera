import xml.etree.cElementTree as ET
import sqlite3

conn = sqlite3.connect("Assignment_week3.sqlite")
cur = conn.cursor()

cur.executescript('''   DROP TABLE IF EXISTS Artist;
                        DROP TABLE IF EXISTS Album;
                        DROP TABLE IF EXISTS Track;
                        DROP TABLE IF EXISTS Genre;

                        CREATE TABLE Artist
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);

                        CREATE TABLE Genre
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);

                        CREATE TABLE Album
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE,
                             artist_id INTEGER);

                        CREATE TABLE Track
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE,
                             len INTEGER, rating INTEGER, count INTEGER,
                             album_id INTEGER, genre_id INTEGER);
                        ''')

fname = raw_input("Enter file name: ")
if len(fname)<1 : fname = "Library.xml"


def lookup (d, key_text):
    found = False
#
    for child in d:
        if found: return child.text
        if child.tag == "key" and child.text == key_text: found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict")
print "Dict count:", len(all)
for entry in all:
    if (lookup(entry, "Track ID") is None) : continue

    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    genre = lookup(entry, "Genre")
    count = lookup(entry, "Play count")
    rating = lookup(entry, "Rating")
    lenght = lookup(entry, "Total Time")

    if name is None or artist is None or album is None or genre is None: continue

    print "Name:",name,"--  Artist:", artist,"-- Album:", album,"--  Play count:", "-- Genre:", genre, count,"--  Rating:", rating,"--  Total Time:", lenght

    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist, ))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
    cur.execute("SELECT ID FROM Genre WHERE name = ?", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ?)", (album, artist_id))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album, ))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)", (name, album_id, genre_id, lenght, rating,count))


    conn.commit()

cur.execute('''SELECT Track.title as Track, Artist.name as Artist, Album.title as Album, Genre.name as Genre
                FROM Track JOIN Genre JOIN Album JOIN Artist
                ON Track.genre_id = Genre.ID and Track.album_id = Album.id
                AND Album.artist_id = Artist.id
                ORDER BY Artist.name, Track.title LIMIT 3''')

conn.commit()
