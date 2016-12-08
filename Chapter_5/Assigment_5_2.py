largest = None
smallest = None



while True:
    num = raw_input("Enter a number: ")
    
    
    
    if num == "done" : break
    if len(num)<1 : break

    try:
		num = int(num)
    except:
		print "Invalid input"
		continue
        
    if smallest is None or num < smallest:
        smallest = num
        
    if largest is None or num > smallest:
        largest = num      
        
        
        
print "Maximum is", largest        
print "Minimum is", smallest         
