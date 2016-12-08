
num_list = list()

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
	    
    if len(num)<1 :
        print "empty number, try again" 
        continue     
       
    try:
		num = int(num)

    except:
		print "Invalid input, please enter integer "
		continue


# 		quit()
    num_list.append(num)
print num_list
print len(num_list)
print max(num_list)
print min(num_list)

   

    
