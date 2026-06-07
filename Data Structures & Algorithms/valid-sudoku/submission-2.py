from collections import defaultdict


class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # check rows
    for row in board:
      frequency = defaultdict(int)
      for num in row:
        if num == ".":
          continue
        frequency[num] += 1
        if frequency[num] > 1:
          return False

    # check columns
    for column in range(0, 9):
      frequency = defaultdict(int)
      for rowIndex in range(0, 9):
        num = board[rowIndex][column]
        frequency[num] += 1
        if frequency[num] > 1 and num != ".":
          return False

    # check squares
    frequency = defaultdict(int)
    for column in range(0, 9):
      for row in range(0, 9):
        if board[column][row] == '.':
            continue
        square = []
        square.append(str(column // 3))
        square.append(str(row // 3))
        square.append(board[column][row])
        key = "".join(square)
        frequency[key] += 1
        if frequency[key] > 1:
            return False
    return True