import Program1, Program2, Program3

def test_charcount():
  assert Program1.charcount("The Simpsons") == {'t': 1, 'h': 1, 'e': 1, ' ': 1, 's': 3, 'i': 1, 'm': 1, 'p': 1, 'o': 1, 'n': 1}, "It should return a dictionary; is it case sensitive?"
  assert Program1.charcount("Don't Panic!") == {'d': 1, 'o': 1, 'n': 2, "'": 1, 't': 1, ' ': 1, 'p': 1, 'a': 1, 'i': 1, 'c': 1, '!': 1}, "It should return a dictionary; is it case sensitive?"
  assert Program1.charcount("Dollhouse Do-Over") == {'d': 2, 'o': 4, 'l': 2, 'h': 1, 'u': 1, 's': 1, 'e': 2, ' ': 1, '-': 1, 'v': 1, 'r': 1}, "It should return a dictionary; is it case sensitive?"

def test_exponents():
  assert Program2.exponents(4) == {2: 16, 3: 81, 4: 256, 5: 625, 6: 1296, 7: 2401, 8: 4096, 9: 6561, 10: 10000, 11: 14641}, "It should return a dictionary"
  assert Program2.exponents(2) == {2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121}, "It should return a dictionary"
  
bag1 = {'Potion': 10, 'Hyper Potion': 7, 'Ultra Ball': 50, 'Rare Candy': 5, 'Nugget': 2}
bag2 = {'Super Potion': 8, 'Ultra Ball': 38, 'Bicycle': 1}
championloot = ['Rare Candy', 'Ultra Ball', 'Max Revive', 'Ultra Ball', 'Rare Candy', 'Ultra Ball']
winloot = ['Potion', 'Super Potion', 'Potion', 'Revive']

def test_addtobag():
  assert Program3.addtobag(bag1.copy(), championloot) == {'Potion': 10, 'Hyper Potion': 7, 'Ultra Ball': 53, 'Rare Candy': 7, 'Nugget': 2, 'Max Revive': 1}, "It should return a dictionary; make sure you're adding to already existing values instead of resetting them (the setdefault method is helpful here)"
  assert Program3.addtobag(bag2.copy(), championloot) == {'Super Potion': 8, 'Ultra Ball': 41, 'Bicycle': 1, 'Rare Candy': 2, 'Max Revive': 1}, "It should return a dictionary; make sure you're adding to already existing values instead of resetting them (the setdefault method is helpful here)"
  assert Program3.addtobag(bag2.copy(), winloot) == {'Super Potion': 9, 'Ultra Ball': 38, 'Bicycle': 1, 'Potion': 2, 'Revive': 1}, "It should return a dictionary; make sure you're adding to already existing values instead of resetting them (the setdefault method is helpful here)"
  
