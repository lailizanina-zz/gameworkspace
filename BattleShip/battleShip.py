#Battle ship game by CodeAcademy!
from random import randint

#This is the board
board = []
for i in range(5):
  board.append(['O'] * 5)

#this makes the colomns be right above each other  
  def print_board(board_in):
    for row in board:
        print(" ".join(row))

#Here we hide our battleship in a random location on the board
def random_row(board_in):
  return randint(0, len(board_in) - 1)
print(board)
def random_col(board_in):
  return randint(0, len(board_in) - 1)
print(board)

#storing players guesses!
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

#the n of chances to guess
for turn in range(5):
#Cooordinate found?
    if guess_row == random_row and guess_col == random_col:
        print("Congratulations! You sank my battleship!") 
        break
    #end of the turns
else:
  if guess_row not in range(5) or \
    guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
  elif guess_row and guess_col == board: 
  	print("You guessed that one already.")
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    
    print("Turn", turn + 1)
    print_board(board)
