def mul(numlist)->int:
    result=numlist[0]
    for i in range(1,len(numlist)):
        result*=numlist[i]
    return result   