def facti(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def s(a,*b):
    res=a
    for j in b:
        res=res+j
    return res
def E(d):
    if((d%2)==0):
        return "Even"
    else:
        return "Odd"
