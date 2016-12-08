import urllib

img = urllib.urlopen("http://www.py4inf.com/cover.jpg").read()
fhand = open("cover.jpg", "w")
fhand.write(img)
fhand.close()



# This program reads all of the data in at once
# across the network and stores it in the variable img
# in the main memory of your computer,
# then opens the file cover.jpg and
# writes the data out to your disk.
# This will work if the size of the file
# is less than the size of the memory of your computer
