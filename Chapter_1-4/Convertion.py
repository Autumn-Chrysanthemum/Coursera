
inp = raw_input("Type a number:\n")
try:    
    print str((float(inp)-32.0)*5.0/9.0)
except:
    print "not number"