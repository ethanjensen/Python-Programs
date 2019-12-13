M = [[1,0,0],[1,1,1],[1,2,4]]
#Calculates the inverse for a specified square matrix M.

def mslice(M, r, c):
    N = []
    for row in M:
        newrow = row[::]
        N.append(newrow)
    N.pop(r)
    for column in N:
        column.pop(c)
    return N

def is_square(M):
    square = True
    for row in M:
        if len(row) != len(M):
            square = False
    return square

def det(M):
    result = 0
    if is_square(M):
        if len(M) == 1:
            return M[0][0]
        else:
            for i in range(0,len(M[0])):
                result = result + pow(-1,i)*M[0][i]*det(mslice(M,0,i))
    else:
        print("Not a square matrix!")
        result = None
    return result

def deepcopy(M):
    N = []
    for i in range(0,len(M)):
        N.append([])
        for j in range(0,len(M[i])):
            N[i].append(M[i][j])
    return N

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

def inverse(M):
    N = []
    for i in range(0,len(M)):
        N.append([])
        for j in range(0,len(M[i])):
            N[i].append(det(mslice(M,i,j))/det(M)*pow(-1,(i+j)))
    N = transpose(N)
    return N

print(inverse(M))
