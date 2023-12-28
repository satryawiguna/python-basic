x = "My name is {}"
y = "My name is {} and she is my wife, {}"
z = "She is {b} and she is {a} wife"

print(x.format("Satrya Wiguna"))
print(y.format("Satrya Wiguna", "Erna Widhiastuti"))
print(z.format(a = "Satrya Wiguna", b = "Erna Widhiastuti"))

a = "Satrya Wiguna"
print(a[2])
print(a[:6])
print(a[7:])
print(a[::2])

b = "Erna Widhiastuti"
c = b.split()
print(c)