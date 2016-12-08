while True:
    line= raw_input("> ")
    if len(line)>0 and line[0] == "#":
        continue
    if line == "Done":
        break
    print line
print "Done!!!!!!!"