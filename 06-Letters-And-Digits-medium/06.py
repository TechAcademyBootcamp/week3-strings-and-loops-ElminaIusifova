sentence = input("Enter your sentence: ")
number=0
letter=0

for i in sentence:
    if i.isdigit():
        number += 1
    elif i.isalpha():
        letter += 1

print("Numbers: ", number)
print("Letters: ", letter)
