
numbers={
    'one':1, 'two':2, 'three':3
    }

for english, num in numbers.items():
    print("{} begins with \"{}\"".format(english.rjust(5), num))