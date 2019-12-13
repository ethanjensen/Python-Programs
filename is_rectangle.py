M = [[1,2,3],[2,0,1],[5,5,6],[-3,4,4]]
#Calculates whether a specified matrix M is a rectangular matrix

def is_rectangle(M):
    rect = True
    row_length = len(M[0])
    for i in range(0, len(M)):
        if (len(M[i]) != row_length):
            rect = False
    return rect

print(is_rectangle(M))
