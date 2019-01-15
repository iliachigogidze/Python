class Polynomial:
    def __init__(self, *coefs):
        self.coefs = coefs

    def __add__(self, other):
        return Polynomial(*(a+b for a, b in zip(self.coefs, other.coefs)))

p1 = Polynomial(1,2,3)
print(p1.coefs)
p2 = Polynomial(4,5,6)
print((p1+p2).coefs)




