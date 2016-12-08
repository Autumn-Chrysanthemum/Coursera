largest = None
print "Before:", largest
for IterVal in [3,41,12,9,74,15]:
    if largest is None or IterVal > largest:
        largest = IterVal
    print "Loop:", IterVal, largest
print "Largest:", largest