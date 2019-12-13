M = [[1,2,3],[0,1,1],[1,2,0]]
#Produces a deep copy of a specified matrix M

def deepcopy(M):
    N = []
    for i in range(0,len(M)):
        N.append([])
        for j in range(0,len(M[i])):
            N[i].append(M[i][j])
    return N

N = deepcopy(M)
N.append([1,4,5,6])
print(N)
print(M)
