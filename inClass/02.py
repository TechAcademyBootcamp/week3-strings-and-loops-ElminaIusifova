# Task1: Create a function that accepts 5 values from the user, adds their squares to the list, and then return that list.
def myFunction():
    array = []
    i = 0
    while i < 5:
        i += 1
        value = int(input("Enter your number: "))
        array.append(value)


    return array

print(f"My new list is {myFunction()}")
