class A:
    l = [10, 20]  # class attribute


b = A()
c = A()
d = A()

b.l.append(30)

print(b.l)
print(c.l)
print(d.l)

e = A()
print(e.l)

print(A.l)
# c.num = 10
# print(id(b.num))
# print(id(c.num))
# print(id(d.num))