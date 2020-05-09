word = input("Enter your favorite word: ")
length = len(word)
if length < 2:
     print("Empty string")
else:
   print("Your new word is: ", word[0]+word[1]+word[-2]+word[-1])


