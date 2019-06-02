#ask user for name

name = input("What is your name?: ")
#ask user for age

age = input("What is your age?: ")

#ask user for city
city = input("What city do you live in?: ")

#ask user what they enjoy
love = input("What do you love doing?: ")

#create output text
answer = "YOur name is {} and you are {} years old. You live in {} and you love {}"
output = answer.format(name, age, city, love)

#print output to screen
print(output)
