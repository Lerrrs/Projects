import random


def guess(x):
  random_number = random.randint(1, x)
  guess = []
  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      print('Sorry thats too low')
    elif guess > random_number:
      print('Sorry thats too High')
 
  print(f'Heck yea, you guessed the right number {random_number}')

guess(10)
    