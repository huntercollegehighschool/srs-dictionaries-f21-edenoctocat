from Program1 import charcount
from Program2 import exponents
from Program3 import addtobag

program = input("Which program(1, 2, or 3)? ")

if program == '1':
  message = input("Enter a message: ")
  print(charcount(message))

elif program == '2':
  exponent = int(input("Number/power: "))
  print(exponents(exponent))

elif program == '3':
  currentbag = {'Potion': 3, 'Revive': 5, 'Dawn Stone': 2, 'Fossilized Drake': 2} #you can change this dictionary to be sure the function works properly
  championsloot = ['Max Revive', 'Max Revive', 'Hyper Potion', 'Revive', 'Fossilized Drake'] #you can change this list to be sure the function works properly
  print(addtobag(currentbag, championsloot))
