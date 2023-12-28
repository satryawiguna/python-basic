x = 1
y = 2

if x < y:
    print("You're correct")
else:
    print("you're not lucky dude")

a = 3

if a < 2:
    print("You're get in to trap 1")
elif a >= 2 and a < 5:
    print("You're get in to trap 2")
else:
    print("You're free")

x = [1,2,3,4,5,6,7,8,9,10]

for item in x:
    print(item)

y = {'satrya': 10, 'wiguna': 20, 'erna': 30, 'widhiastuti': 40}

for item in y:
    print(y[item])

z = [(1,2),(3,4),(5,6)]

template = "{x} - {y}"
for tupOne, tupTwo in z:
    print(template.format(x = tupTwo, y = tupOne))


i = 0

while i < 10:
    print("i is {}".format(i))
    i += 1

print(list(range(0, 5)))
print(list(range(0, 20, 2)))

for item in range(10):
    print(item)


x = [1,2,3,4,5]
y = []
for item in x:
    y.append(item**2)
print(y)

z = [item ** 2 for item in x]
print(z)