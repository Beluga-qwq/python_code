p=int(input('输入当月利润:'))
b=0
t=[100000,100000,200000,200000,400000]
r=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(6):
    if p <= t[i]:
        b+=p*r[i]
        p=0
        break
    else:
        b+=t[i]*r[i]
        p-=t[i]
b+=p*r[-1]
print(b)
