
is_active = True

while is_active:

    command = input("Number ->")

    if command == "quit":
        is_active = False
        continue
    
    number = int(command) #typecasting

    #Your code here
    if number > 18:
        print("Person is an adult")
    
    elif number > 3 and number < 6:
        print("Person is in preschool")

    elif number >= 14 and number < 18:
        print("Person is in High School")

    elif number > 10 and number < 14:
        print(f""" Person {number} years old is in Middle school """)

    elif number < 4:
        print(f""" Person {number} years old is an infant """)

    else:
        print(f""" Person {number} years old is in Grade school """)

    

    

print("Have a nice day!")
