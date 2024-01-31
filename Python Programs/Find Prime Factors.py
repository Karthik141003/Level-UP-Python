def prime(n):
    res=[]
    i=2
    a=n
    while(a>i):
        if n%i==0:
            res.append(i)
            n=n//i
        else:
            i+=1
            continue
    return res

a=int(input())
c=prime(a)
print("The Prime Factors are:")
print(c)
