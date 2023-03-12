def t(n):
    l=[]
    for i in range(n):
        if i==0:
            l.append([1])
        elif i==1:
            l.append([1,1])
        else:
            y=[]
            for j in range(i+1):
                if j==0 or j==i:
                    y.append(l[i-1][j]+l[i][j-1])

            l.append(y)
    return l

t(11)
for i in range(len(t(11))):
    print()