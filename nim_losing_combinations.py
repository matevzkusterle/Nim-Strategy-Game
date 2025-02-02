board = [3,5,7]

def f():
    s = []
    for i in range(board[0]+1):
        for j in range(board[1]+1):
            for k in range(board[2]+1):
                if i ^ j ^ k == 0:
                    s.append([i,j,k])
    return s

f()