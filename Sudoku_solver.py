S=[[2, 0, 0, 3, 0, 0, 0, 0, 5],
[0, 3, 0, 0, 0, 4, 2, 1, 0],
[1, 9, 8, 0, 0, 0, 4, 6, 0],
[0, 5, 7, 4, 0, 2, 1, 0, 0],
[0, 0, 4, 0, 8, 0, 3, 0, 0],
[0, 0, 1, 6, 0, 9, 7, 8, 0],
[0, 1, 3, 0, 0, 0, 5, 4, 7],
[0, 8, 2, 7, 4, 6, 0, 3, 0],
[4, 7, 9, 0, 0, 3, 0, 0, 8]]

def sudoku_solve(S,bC,bV,r,oldCoords):

    coords = None
    if not oldCoords:
        coords = find_empty(S)
        if not coords:
            sudoku_print(S,"S")
            return True

    else:
        coords = oldCoords

    i,j = coords


    happened = False
    #print("r: ", r)
    for h in range(r,10):

        if sudoku_check(S, h, (i,j)):
            S[i][j] = h
            bV.append(h)
            bC.append(coords)
            happened = True
            # print("common")
            # print("h: ", h)
            # print("coords: ", coords)
            # print("bV: ", bV)
            # print("bC: ", bC )
            # sudoku_print(S,"S")
            # print("common")
            # print("______________________________")

            break

#BackTracking
    if happened == False:


        oldCoords = bC.pop(len(bC) - 1)
        r = bV.pop(len(bV) - 1) + 1
        if r > 9:
            r = 9
        S[oldCoords[0]][oldCoords[1]] = 0
        # print("BackTracking")
        # print("bV: ", bV)
        # print("bC: ", bC )
        # print("r: ", r)
        # print("oldCoords: ", oldCoords)
        # sudoku_print(S,"S")
        # print("BackTracking")
        # print("______________________________")

    else:
        r = 1
        oldCoords = None


    sudoku_solve(S,bC,bV,r,oldCoords)

def find_empty(S):
    for i in range(0, 9):
        for j in range(0, 9):
            if S[i][j] == 0:
                return (i, j)
    return None

def sudoku_check(S, x, z):

    for p in range(0, 9):
        if S[z[0]][p] == x and z[1] != p:
            return False


    for p in range(0, 9):
        if S[p][z[1]] == x and z[0] != p:
            return False


    Q_i = z[1]//3
    Q_j = z[0]//3
    for p in range(Q_j*3, Q_j*3 + 3):
        for q in range(Q_i*3, Q_i*3 + 3):
            if S[p][q] == x and (p,q) != z:
                return False

    return True




def sudoku_print(S,num):
    print('\n' + num + ':')
    for i in range(0, 9):
        for j in range(0, 9):
            if (j % 3 == 2):
                nend = "  "
            else:
                nend = " "

            if (i % 3 == 2):
                nend2 = "\n\n"
            else:
                nend2 = "\n"


            if (j == 8):
                print(S[i][j], end=nend2)
            else:
                print(S[i][j], end=nend)




def board_check(S):

    for n in range(0, 9):
        for m in range(0,9):
            x = S[n][m]
            # print("pos: ", n, m)
            if x != 0:
                for p in range(0, 9):
                    if S[n][p] == x and m != p:
                        # print("Saida:", 1)
                        return False


                for p in range(0, 9):
                    if S[p][m] == x and n != p:
                        # print("Saida:", 2)
                        return False


                Q_i = n//3
                Q_j = m//3
                for q in range(Q_j*3, Q_j*3 + 3):
                    for p in range(Q_i*3, Q_i*3 + 3):
                        # print(" p:",p," q:",q," n:",n," m:",m)
                        if S[p][q] == x and (p,q) != (n,m):
                            # print("Saida:", 3)
                            return False

    return True

ra = 1

ra = 1
xa = 0
bC = []
bV = []
r = 1
oldCoords = None

if board_check(S) == False:
    print("Board inválida!")
else:
    sudoku_print(S, "S")
    sudoku_solve(S,bC,bV,r,oldCoords)
    sudoku_print(S, "S")
