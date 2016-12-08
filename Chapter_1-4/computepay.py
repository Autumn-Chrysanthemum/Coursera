import sys

def computepay(hours, rate, overpay):

    if hours > 0 and hours <=40:
        pay = hours*rate
    elif hours > 40:
        pay = 40*rate+(hours-40)*rate*overpay
    else:
        pay = 0
        print "Number of Hours have to be positive"
    return pay    

def check_input(any_raw_input):
    try:
        any_input = float(any_raw_input)
    except:
        print "Not a number"
        sys.exit(1)
    return any_input
    

hours_input = check_input(raw_input("Enter hours:\n"))
rate_input = check_input(raw_input("Enter rate:\n"))
rate_overpay = check_input(raw_input("Enter overpay pate:\n"))


x = computepay(hours_input,rate_input,rate_overpay)    
 
print "You will earn:", x