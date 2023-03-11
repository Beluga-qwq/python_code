flag=0
def check(col,res,row):
    for i in range(row):
        if res[i] == col or res[i]+i==row+col or res[i] -i==col-row:
            return False
    return True

def dfs(num,res,row):
    if row==num:
        print(res)
        return
    for col in range(num):
        if check(col,res,row):
            res[row]=col
            dfs(num,res,row+1)
            res[row]=0

if __name__=='__main__':
    num=int(input('请输入皇后的数量:'))
    res=[0 for _ in  range(num)]
    row=0
    dfs(num,res,row)