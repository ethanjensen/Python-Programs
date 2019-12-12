import math

alphabetlist = ['a','b','c','d','e','f','g','h']

S = [0,2,3,5,6,7,8,9,10,12,14,15]
N = []

def sort(intList):
    i = 0
    while i < len(intList):
        j = i + 1
        while j < len(intList):
            if intList[j] < intList[i]:
                (intList[i], intList[j]) = (intList[j], intList[i])
            j = j + 1
        i = i + 1
    newList = []
    for i in range(0,i):
        if not (intList[i] in newList):
            newList.append(intList[i])
    return newList

def num_bits(intList):
    return math.ceil(math.log(intList[-1]+1,2))


def explode_minterms(intList):
    mintList = []
    n = num_bits(intList)
    for num in intList:
        minterm = [0]*n
        for i in range(0,n):
            if num >= 2**(n-i-1):
                num = num - 2**(n-i-1)
                minterm[i] = 1
        mintList.append(minterm)
    return mintList

def combine_minterms(mintList):
    new_mintList = []
    num_bits = len(mintList[0])
    beencombined = [0]*len(mintList)
    for i in range(0, len(mintList)):
        print(mintList)
        for j in range(i+1, len(mintList)):
            comparison_list = [0]*num_bits
            for z in range(0, num_bits):
                if (mintList[i][z] == mintList[j][z]):
                    comparison_list[z] = 1
            if comparison_list.count(0) == 1:
                minterm = []
                beencombined[i] = 1
                beencombined[j] = 1
                for k in range(0,num_bits):
                    if comparison_list[k] == 1:
                        minterm.append(mintList[i][k])
                    else:
                        minterm.append(2)
                if minterm not in new_mintList:
                    new_mintList.append(minterm)
    for i in range(0, len(mintList)):
        if beencombined[i] == 0:
            new_mintList.append(mintList[i])
    return new_mintList

def reduce_minterms(intList):
    oldMintList = explode_minterms(intList)
    newMintList = []
    while oldMintList != newMintList:
        newMintList = oldMintList
        oldMintList = combine_minterms(newMintList)
    return newMintList

def interpret_minterms(mintList):
    num_bits = len(mintList[0])
    for i in range(0, len(mintList)):
        for j in range(0, num_bits):
            if mintList[i][j] != 2:
                print(alphabetlist[j], end ='')
            if mintList[i][j] == 0:
                print("'",end='')
        print(" + ", end = '')

S = sort(S)
print(reduce_minterms(S))
print("")
print(interpret_minterms(reduce_minterms(S)))
