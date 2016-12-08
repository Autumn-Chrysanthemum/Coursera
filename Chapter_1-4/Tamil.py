fname = raw_input("Enter file name: ")
try:
    fh = open('romeo.txt')
except:
    print "File",fname,"does not exist"
    quit()

lst = list()
main_list = list()

for line in fh:
    line = line.rstrip()
    line = line.split("\n")
    list_element = list()

    for element in line:
        list_element = element.split()
        print element

    for item in list_element:
        if item not in main_list:
            main_list.append(item)

main_list.sort()
print main_list