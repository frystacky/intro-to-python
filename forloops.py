vowels = 0
consonants = 0

for number in range(1, 2):
    print(number)

for letter in "Hello my name is bob!":
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter == "":
        pass
    else:
        consonants += 1
        
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

