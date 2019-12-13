M = [[1,2,3],[0,1,1],[1,2,0],[4,4,5]]
#Calculates the transpose for a specified matrix M.

def is_rectangle(M):
    rect = True
    row_length = len(M[0])
    for i in range(0, len(M)):
        if (len(M[i]) != row_length):
            rect = False
    return rect

def transpose(M):
    T = []
    if (is_rectangle(M)):
        column_length = len(M[0])
        row_length = len(M)
        for i in range (0, column_length):
            T.append([])
            for j in range (0, row_length):
                T[i].append(M[j][i])
    else:
        print("Non-rectangular matrix!")
    return T

print(transpose(M))
