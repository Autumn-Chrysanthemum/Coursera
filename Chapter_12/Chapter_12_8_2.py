import urllib

img = urllib.urlopen("http://www.py4inf.com/sover.jpg")
fhand = open("cover.jpg", "w")

size = 0
while True:
    info = img.read(100000)
    if len(info)<1: break
    size = size + len(info)
    fhand.write(info)

print size, "characters copied."
fhand.close()


# In order to avoid running out of memory,
# we retrieve the data in blocks (or buffers)
# and then write each block to your disk before
# retrieving the next block.

# In this example, we read only 100,000 characters at a time
# and then write those characters to the cover.jpg file
# before retrieving the next 100,000 characters of data from the web.

# Mac has build-in (curl == "copy URL"):
# curl -O http://www.py4inf.com/cover.jpg
