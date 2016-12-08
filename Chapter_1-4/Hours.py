

try:
    hours_string = raw_input("Enter Hours:\n")
    hrs = float(hours_string)
          
except:
    print "Not a number" 
    quit()
try:
    rate_string = raw_input("Enter Rate:\n")
    rate = float(rate_string)
          
except:
    print "Not a number" 
    quit()
if hrs > 0:
    if hrs < 40:
        pay = hrs * 10
    else:
        pay = (hrs-40)*rate*1.5+40*rate
print pay
    

