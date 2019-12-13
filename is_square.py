M = [[1,2,3],[0,1,1],[1,2,0]]
#Determines whether a specified matrix M is square.

def is_square(M):
    square = True
    for row in M:
        if len(row) != len(M):
            square = False
    return square

print(is_square(M))
