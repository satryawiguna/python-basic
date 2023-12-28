def my_first_func(param = "Default"):
    """
    THIS IS DESCRIPTION OF FUNCTION
    """
    print("Welcome to my first function: {}".format(param))

my_first_func("Satrya Wiguna")

def hello_world_func():
    return "HELLO WORLD"

helloWorld = hello_world_func()
print(helloWorld)

def add_numbebr_func(value1, value2):
    return value1**2 + value2**4

result = add_numbebr_func(4, 8)
print(result)

a = [1,2,3,4,5,6,7,8,9]

def even_bool_func(num):
    return num%2 == 0

result = filter(even_bool_func, a)
print(list(result))

result = filter(lambda num:num%2 == 0, a)
print(list(result))

print('x' in [1,2,3])
print('x' in [1,2,3,'x'])