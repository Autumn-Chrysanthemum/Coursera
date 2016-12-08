# For example, suppose you have a list of words and 
# you want to sort them from longest to shortest

txt = "but soft what light in yonder window breaks"
words = txt.split()
print type(words), words
t = list()
for word in words:
    t.append((len(word), word))
    print t
    t.sort(reverse=True)
print type(t), t
res = list()
for length, word in t:
    res.append(word)
print res
for item in res:
    print item