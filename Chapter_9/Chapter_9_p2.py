# you are given a string and you want to count
# how many times each letter appears
# using GET


word = raw_input("Please type a word:\n")
if len(word)< 1: word = "condition"

my_dict = dict()
for letter in word:
    my_dict[letter]= my_dict.get(letter,0) + 1
print my_dict