# Task 2. Write a program that prints the negative numbers and their indexes in the list.
array = [3, 6, -3, -9, 0, 10, -11]

for i in array:
    array.index(i)
    # print(array.index(i))
    if i < 0:
        print(f"The index of {i} is {array.index(i)} ")
    else:
        pass






