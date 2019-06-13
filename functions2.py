def about(name, age, likes):
        sentence = "Meet {}! They are {} years old and they like {}".format(name, age,likes)
        return sentence

about("jack", 23, "Phython")

about(age = 23, name = "Jack", likes = "Python")

def about(name, age, likes = "Python"): #defualt value and must come last
        sentence = "Meet {}! They are {} years old and they like {}".format(name, age,likes)
        return sentence
