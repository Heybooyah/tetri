
def updateBoard(temp,board):
    print(board)
    s = ""
    mixedboard = board
    pos = [0,0]
    for i in temp:
        for ii in i:
            if ii != 0:
                mixedboard[pos[0]][pos[1]] = ii
            if (pos[1] == 9):
                pos[1] = 0
                pos[0] += 1
            else:
                pos[1] += 1
    for i in mixedboard:
        for c in i:
            if (c == 0):
                s += "\033[38;5;240m\u2588\u2588"
            if (c == 1):
                s += "\033[38;5;208m\u2588\u2588"
            if (c == 2):
                s += "\033[38;5;4m\u2588\u2588"
            if (c == 3):
                s += "\033[38;5;51m\u2588\u2588"
            if (c == 4):
                s += "\033[38;5;226m\u2588\u2588"
            if (c == 5):
                s += "\033[38;5;201m\u2588\u2588"
            if (c == 6):
                s += "\033[38;5;82m\u2588\u2588"
            if (c == 7):
                s += "\033[38;5;196m\u2588\u2588"
        print(s)
        s = ""
    print("-----------------------------------")