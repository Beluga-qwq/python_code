# a=0
# l=[]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if((i!=j)and(j!=k)and(k!=i)):
#                 print(f"{i}{j}{k}")
#                 a+=1
# print(a)

import itertools
sum=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum+=1
print(sum)