lagest_so_far=-1
print "Before", lagest_so_far
for the_num in [9,41,12,3,74,15]:
    if the_num > lagest_so_far:
        lagest_so_far=the_num
    print lagest_so_far, the_num
print "After", lagest_so_far