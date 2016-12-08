#word = 'banana'


def count(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print count

ask = raw_input("Enter string or letter:\n")

x = count(ask)

