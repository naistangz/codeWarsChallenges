# def sayMeOperations(stringNumbers):
#     starting_index = stringNumbers[2]
#     if starting_index == stringNumbers[0] + stringNumbers[1]:
#         return "addition"
#     elif starting_index == stringNumbers[0] - stringNumbers[1]:
#         return "subtraction"
#     elif starting_index == stringNumbers[0]/stringNumbers[1]:
#         return "division"
#     elif starting_index == stringNumbers[0]*stringNumbers[1]:
#         return "multiplication"


# sayMeOperations("1 2 3 5 8")

# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# letter_to_points = {k:v for k, v in zip(letters, points)}
# print(letter_to_points)

# letter_to_points[" "] = 0
# print(letter_to_points)

# def score_word(word):
#   point_total = 0
#   for letter in word:
#     point_total += letter_to_points[letter]
#   return point_total

# brownie_points = score_word("BROWNIE")
# print(brownie_points)

# player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "lexi_Con":["ERASER", "BELLY", "HUSKY"], "Prof_Reader":["ZAP", "COMA", "PERIOD"]}

# player_to_points = {k:v for k, v in player_to_words.items()}


# print(player_to_points)
# Write your sum_values function here:
def sum_values(my_dictionary):
  counter = 0
  for v in my_dictionary.values():
    counter += my_dictionary[v]
  return counter
  
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))


