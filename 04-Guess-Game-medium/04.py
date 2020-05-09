print("Welcome to Guessing Game!")
num = 3
iterator = 0
is_win = False
while iterator < 3:
  iterator+=1
  guess_num=int(input("Guess the number: "))
  if guess_num==num:
    print("Congratulations! Well guessed!")
    break
  else:
    print("Wrong number")
else:
   print("The game is over")
