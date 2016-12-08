# Tuples are immutable
# Comparing tuples

t = ("a","b","c","d","e")
t1 = ("a",)
t3 = tuple()
t4 = tuple("lupins")

print type(t1), t1
print t3
print type(t), t
print type(t4), t4
print t[3]

print t[1:3]
# t[0] = "A"
t5 = ("A",) + t[1:]
print t5, t

t6 = (0,1,2)
t7 = (0,3,4)

print t6 < t7