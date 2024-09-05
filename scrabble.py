# First draft completed September 5, 2024
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_letters_points = zip(letters, points)
letter_to_points = {key:value for key, value in zipped_letters_points}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# OLD APPROACH - Turns each word into one long string and calculates points
'''
player_to_points = {}
for player, words in player_to_words.items():
  joined_words = ''.join(words)
  player_points = 0
  player_points += score_word(joined_words)
  player_to_points[player] = player_points
'''

# NEW APPROACH - Calculates points for each individual word, for each player
# Fits much better with the logic of `scrabble`
player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
       player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)

# ADDITIONAL TASKS
# Create a function that would take in a player and a word, and add that word to the list of words they’ve played
  #Completed: 
# Turn your update player points nested loops into a function that you can call any time a word is played
  #Completed: 
# Make your letter_to_points dictionary able to handle lowercase inputs as well
  #Completed: 