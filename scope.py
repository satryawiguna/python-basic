x = 5

def my_first_func(x):
    print("x value before is:", x)
    x = 100
    print("x value after is:", x)

my_first_func(x)
print("x value global is:", x)

y = 5

def my_second_func():
    global y
    print("y value before is:", y)
    y = 100
    print("y value after is:", y)

my_second_func()
print("y value global is:", y)

z = 5

def my_third_func():
    return 1000

print("z value before is:", z)
z = my_third_func()
print("z value after is:", z)