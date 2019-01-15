class Polynomial:
    def __init__(self, *coefs):
        self.coefs = coefs

    def __add__(self, other):
        return Polynomial(*(a+b for a,b in zip(self.coefs, other.coefs)))

    def __len__(self):
        return len(self.coefs)

p1 = Polynomial(2,3,4,6)
p2 = Polynomial(1,2,3)
print((p1 + p2).coefs)
print(len(p1))