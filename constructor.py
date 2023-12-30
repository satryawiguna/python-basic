class MyFirstClass():
    def __init__(self) -> None:
        pass

x = MyFirstClass()
print(type(x))

class MySecondClass():
    def __init__(self, param_one) -> None:
        self.param_one = param_one

y = MySecondClass(param_one = 'valueOne')
print(type(y))
print(y.param_one)

class MyThirdClass():
    def __init__(self, param_one) -> None:
        self.param_one = param_one

y = MySecondClass(param_one = 'valueOne')
print(type(y))
print(y.param_one)
