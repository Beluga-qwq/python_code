#题目 斐波那契数列。
#程序分析 斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。图方便就递归实现，图性能就用循环。
def fb(n):
    if n<=2:
        return 1
    else:
        return fb(n-1)+fb(n-2)
print(fb(100))
