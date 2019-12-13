M = [[2,1,0,0],[0,2,2,0],[1,0,1,3],[1,1,1,1]]
b = [228,228,114,195]
#Calculates the solution to a specified linear system, Mx = b, by elimination.

def deepcopy(M):
    N = []
    for i in range(0,len(M)):
        N.append([])
        for j in range(0,len(M[i])):
            N[i].append(M[i][j])
    return N

def findsolutions(oldM,oldb):
    M = deepcopy(oldM)
    b = oldb[::]
    n = len(M)
    for i in range(0,n-1):
        for j in range(i+1,n):
            pivot1 = M[i][i]
            pivot2 = M[j][i]
            if pivot1 == 0:
                (M[i],M[j]) = (M[j],M[i])
            if pivot2 != 0:
                for k in range(i,n):
                    M[i][k] *= pivot2
                for k in range(i,n):
                    M[j][k] *= pivot1
                    M[j][k] -= M[i][k]
                b[i] *= pivot2
                b[j] *= pivot1
                b[j] -= b[i]
    for i in range(0,n-1):
        for j in range(i+1,n):
            pivot2 = M[n-1-i][n-1-i]
            pivot1 = M[n-1-j][n-1-i]
            if pivot2 == 0:
                (M[n-1-i],M[n-1-j]) = (M[n-1-j],M[n-1-i])
            if pivot1 != 0:
                M[n-1-i][n-1-i] *= pivot1
                for k in range(0,n):
                    M[n-1-j][n-1-i-k] *= pivot2
                    M[n-1-j][n-1-i-k] -= M[n-1-i][n-1-i-k]
                b[n-1-i] *= pivot1
                b[n-1-j] *= pivot2
                b[n-1-j] -= b[n-1-i]
    for i in range(0,n):
        b[i] /= M[i][i]
    return b

print(findsolutions(M, b))
