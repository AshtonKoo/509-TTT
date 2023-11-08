from logic import get_winner

# X win
test_board = [[None,"O","X"],["O",None,"X"],[None,None,"X"]]
winner = get_winner(test_board)
print(winner)

# O win
test_board = [["O","O","X"],["O",None,"X"],["O",None,"X"]]
winner = get_winner(test_board)
print(winner)

# Draw
test_board = [[None,"O","X"],["O",None,"X"],["O","O",None]]
winner = get_winner(test_board)
print(winner)
