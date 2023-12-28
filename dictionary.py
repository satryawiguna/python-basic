MyFirstDictionary = {'key1': 'value1', 'key2': 'value2'}
print(MyFirstDictionary)
print(MyFirstDictionary['key1'])

MySecondDictionary = {'key1': 'value1', 'key2': 'value2', 'key3': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2', 'subkey3': [1, 3, 5]}}
print(MySecondDictionary['key3']['subkey3'][1])

MyThirdDictionary = {'key1': 'value1', 'key2': 'value2'}
print(MyThirdDictionary)
MyThirdDictionary['key3'] = 'value3'
print(MyThirdDictionary)
