while True:
    line= raw_input("> ")
    if line.startswith("#"):
        continue
    if line == "Done":
        break
    print line
print "Done!!!!!!!"