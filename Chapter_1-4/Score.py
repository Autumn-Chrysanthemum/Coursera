
try:
    score = raw_input("Enter Score: ")
    score_f = float(score)

except:
    print "Score should be digits"
    quit()

def computegrade (score_f):
    if score_f > 1.0 or score_f < 0.0:
        print "Score should be between 0.0 and 1.0"
        quit()
    else:
    
        if score_f >= 0.9:
    	    return "A"
        elif score_f >= 0.8:
    	    return "B"
        elif score_f >= 0.7:
    	    return "C"
        elif score_f >= 0.6:
    	    return "D"
        else:
            return "F"

x = computegrade(score_f)

print x
