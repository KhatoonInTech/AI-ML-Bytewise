def minus(numlist)->int:
    diff=numlist[0]
    for i in range(1,len(numlist)):
        diff-=numlist[i]
    return diff   