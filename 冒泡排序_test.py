n=list(map(int,input().split(" ")))
def mp(n):
    a=len(n)
    for i in range(0,a):
        for j in range(0,a-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
print(mp(n))