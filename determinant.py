M = [[1,1,1,1],[4,4,2,1],[10,9,3,1],[20,16,4,1]]

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

print(det(M))
