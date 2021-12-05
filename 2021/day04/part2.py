winningSets = [
    [ 0,  1,  2,  3,  4],
    [ 5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [ 0,  5, 10, 15, 20],
    [ 1,  6, 11, 16, 21],
    [ 2,  7, 12, 17, 22],
    [ 3,  8, 13, 18, 23],
    [ 4,  9, 14, 19, 24],
]

def processInput(input):
    drawnNumbers = input[0].split(",")

    boards = []
    i = 2
    while i < len(input)-4:
        board = " ".join(input[i:i+5])
        boards.append(board.split())

        i += 6

    return drawnNumbers, boards


def checkBoard(markedBoard):
    if len(markedBoard) >= 5:
        for set in winningSets:
            for space in set:
                if space not in markedBoard:
                    break
            else:
                return True

    return False


with open("input.txt") as f:
    input = f.readlines()

drawnNumbers, boards = processInput(input)
markedBoards = [[] for _ in boards]
winners = []
draw = 0
for drawNo, draw in enumerate(drawnNumbers):
    for i, board in enumerate(boards):
        if draw in board:
            markedBoards[i].append(board.index(draw))

    if drawNo >= 4:
        for i, markedBoard in enumerate(markedBoards):
            if i not in winners and checkBoard(markedBoard):
                winners.append(i)

    if len(winners) == len(boards):
        break

loser = winners[-1]
losingBoard = boards[loser]
unmarkedSum = 0
for i, number in enumerate(losingBoard):
    if i not in markedBoards[loser]:
        unmarkedSum += int(number)

print(unmarkedSum*int(draw))
