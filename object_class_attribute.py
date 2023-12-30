class MyFirstClass():
    object_attribute_one = "valueTwo"

    def __init__(self, param_one) -> None:
        self.param_one = param_one

x = MyFirstClass(param_one = "valueOne")

print(x.param_one)
print(x.object_attribute_one)