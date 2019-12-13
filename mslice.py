M = [[1,2,3],[0,1,1],[1,2,0]]
#Removes a row at index r and column at index c for a specified matrix M.

def mslice(M, r, c):
    N = []
    for row in M:
        newrow = row[::]
        N.append(newrow)
    N.pop(r)
    for column in N:
        column.pop(c)
    return N

N = mslice(M, 0, 0)
print(N)
print(M)
