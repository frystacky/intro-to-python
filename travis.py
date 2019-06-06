known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi! my name is Travis")
    name = input("What is your name? ").strip().capitalize()
    
    if name in known_users:
        print("Hello, {}".format(name))
        remove = input("Would you like to be removed from the system (y/n)").lower()
        
        if remove == "y":
            #print(known_users)
            known_users.remove(name)
            #print(known_users)
        elif remove == "n":
            print("no problem, i didnt want you to leave anyways!")
    else:
        print("hmm i dont think you are on the list {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
             #print(known_users)
             known_users.append(name)
             #print(known_users)
        elif add_me == "n":
            print("No worries, see you around!")
