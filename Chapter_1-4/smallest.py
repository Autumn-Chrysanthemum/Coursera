smallest = None
print "Before:", smallest
for IterVal in [3,41,12,9,74,15]:
    if smallest is None or IterVal < smallest:
        smallest = IterVal
    print "Loop:", IterVal, smallest
print "Smallest:", smallest