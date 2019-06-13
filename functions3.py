numbers = [1,2,3,4,5]

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)


print(add(1,2,3,4,5))


def about(name, age,likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age,likes)
    return sentence

dictionary = {"name": "Dan", "age": 28, "likes": "Python"}

print(about(**dictionary)) ##key words need double star


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


foo(huda = "Female", ziyad = "male")

