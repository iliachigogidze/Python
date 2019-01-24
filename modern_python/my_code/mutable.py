mutable = [1, 1, 2, 3, 5, 8]
immutable = (5, 8, 13, 21)

mutable_b = mutable
immutable_b = immutable

mutable += [mutable[-2] + mutable[-1]]
print(mutable)
print(mutable_b)

immutable += (immutable[-2] + immutable[-1],)
print(immutable)
print(immutable_b)