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


def checkBoards(markedBoards):
    for i, markedBoard in enumerate(markedBoards):
        if len(markedBoard) >= 5:
            for set in winningSets:
                for space in set:
                    if space not in markedBoard:
                        break
                else:
                    return i

    return None


with open("input.txt") as f:
    input = f.readlines()

drawnNumbers, boards = processInput(input)
markedBoards = [[] for _ in boards]
winningBoardNo = None
draw = 0
for drawNo, draw in enumerate(drawnNumbers):
    for i, board in enumerate(boards):
        if draw in board:
            markedBoards[i].append(board.index(draw))

    if drawNo >= 4:
        winningBoardNo = checkBoards(markedBoards)
        if winningBoardNo is not None:
            break

winningBoard = boards[winningBoardNo]
unmarkedSum = 0
for i, number in enumerate(winningBoard):
    if i not in markedBoards[winningBoardNo]:
        unmarkedSum += int(number)

print(unmarkedSum*int(draw))
