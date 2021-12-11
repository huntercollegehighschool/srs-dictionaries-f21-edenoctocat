from Program1 import charcount
from Program2 import exponents
from Program3 import addtobag
import json

program = input("Which program(1, 2, or 3)? ")

if program == '1':
  message = input("Enter a message: ")
  print(charcount(message))

elif program == '2':
  exponent = int(input("Number/power: "))
  print(exponents(exponent))

elif program == '3':
  f = open("mybag.txt", "r")
  currentbag = json.load(f)
  f.close()
  lootinput = input("Loot to add to your bag: ")
  championsloot = lootinput.split(", ")
  newbag = addtobag(currentbag, championsloot)
  print(newbag)
  f = open("mybag.txt", "w")
  json.dump(currentbag, f)
  f.close()