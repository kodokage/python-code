from random import  randint
secret = randint(1, 10 ) 

print("Welcome!")

guess = 0
while guess != secret:
  g = input("Guess the number : ")
  guess = int(g)
  if guess == secret:
    print(str(guess) +" : You win!")
  else:
    if (guess >secret):
      print(str(guess) +" : Too High!")
    else:
      print(str(guess) + " : Too Low!")

print("Game Over!")
