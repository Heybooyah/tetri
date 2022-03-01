#Self explanatory imports
import random
import keyboard as kb
import time
import pandas as pd
import tetrisfuncs as tf

#Variable defining
prevpos = [0,4]
table = pd.read_csv("tetrisPieceTables.csv")
table = pd.DataFrame(table)
table = table.values.tolist()
table.insert(0,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
p = 0
bag = [1,2,3,4,5,6,7]
board = []
lines = 0
i = 19

#THERE IS A REALLY GOOD REASON WHY THIS LIST IS DEFINED THIS WAY
#I AM NOT JUST REALLY LAZY, IT CAUSED A MAJOR BUG TO DEFINE IT WITH REPETITION
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

#Actually start the game
while (lines < 3):

    lines += 1
    #Pick a remaining piece from the bag and put it on the map
    if (len(bag) > 1):
        p = bag[(random.randint(1,len(bag))) - 1]
        bag.pop(bag.index(p))
    else:
        p = bag[0]
        bag = [1,2,3,4,5,6,7]
    piecepos = [0,4]

    while True:
        #Reset the temporary board to avoid smearing
        tempboard = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        #Scan over the CSV pixel-by-pixel
        xi = (p - 1) * 4
        safemove = 1
        placer = []
        while xi < p * 4:
            boardsave = tempboard
            yi = 0
            while yi < 4:
            #If a piece is found, place it on the temporary grid
                if (table[yi][xi] != 0):
                    tl = [xi - ((p - 1) * 4) + piecepos[1],yi + piecepos[0]]
                    if (board[tl[1]][tl[0]] == 0):
                        tempboard[tl[1]][tl[0]] = p
                        placer.append(tl)
                    else:
                        safemove = 0
                        tempboard = boardsave
                #Repeat the while loops until the whole piece has been scanned
                yi += 1
            xi += 1
        if (safemove == 0):
            piecepos = prevpos
        #Display the game state
        tf.updateBoard(tempboard,board)
        move = kb.read_key()
        prevpos = piecepos
        if (move == "left"):
            piecepos[1] -= 1
        if (move == "right"):
            piecepos[1] += 1
        if (move == "down"):
            piecepos [0] += 1
        if (move == "space"):
            for pos in placer:
                board[pos[1]][pos[0]] = p
            placer = []
            time.sleep(0.05)
            break
        time.sleep(0.05)
    #1 = L, 2 = J, 3 = I, 4 = O, 5 = T, 6 = S, 7 = Z

 