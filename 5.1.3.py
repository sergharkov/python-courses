
import random
#---------------------------------
def generate_maze(max_rows, max_cols, max_mines):
    NP= [[0 for x in range(max_cols)] for y in range(max_rows)]
    n=max_mines
    while n>0:
        i = random.randint(0, max_rows-1)
        j = random.randint(0, max_cols-1)
        if NP[i][j] != 0:
            continue
        NP[i][j] = -1
        n -=1
    for i in range(max_rows):
        for j in range(max_cols):
            if NP[i][j] == 0:
                N_mines=0
                for k in range (-1,2):
                    for l in range(-1,2):
                        x = i+k
                        y = j+l
                        if  x < 0 or x >= max_rows or y < 0 or y >=max_cols:
                            continue
                        if NP[x][y] < 0:
                            N_mines+=1
                NP[i][j]= N_mines    
    return NP

print(generate_maze(10,15,50))

