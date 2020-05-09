num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))
num4 = int(input("Enter num 4: "))
num5 = int(input("Enter num 5: "))

list = [num1, num2, num3, num4, num5]

odd_number=0
even_number=0

for num in list:
    if num%2 == 0:
        even_number+=1
    else:
        odd_number+=1
print("Odd number: ", odd_number )
print("Even number:", even_number )
