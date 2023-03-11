raw=[]

for i in range(3):
    x=int(input())
    raw.append(x)

def bubble(raw):
    n=len(raw)
    for i in range(n):
        for j in range(1,n-i-1):
            if raw[j]>raw[j+1]:
                raw[j],raw[j+1]=raw[j+1],raw[j]
    return raw

print(bubble(raw))

