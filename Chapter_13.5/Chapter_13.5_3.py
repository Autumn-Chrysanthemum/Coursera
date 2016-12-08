class PartiAnimal_1:
    x = 0
    y = 3

    def party_1(self):
        self.x = self.x + 1
        print "So far:", self.x

na = PartiAnimal_1()

print "Type:", type(na)
print "Dir:", dir(na)