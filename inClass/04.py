# Task3(Hard). Write a Python program to remove duplicates from a list.

list = [4, 5, 6, 3, 1, 4, 5, 6, 7, 4, 6]
print(f"Before dublicates: {list}")

array = []

for i in list:
    if i not in array:
        array.append(i)
print(f"After dublicates: {array}")
