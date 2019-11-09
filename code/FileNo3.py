# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析:
# 1.完全平方数x，则存在且唯一存在正整数a，使得a*a=x
# 2.里面需要用到求平方根，可以用sqrt()函数
import math
# 函数功能：判定maxNum的整数平方根是否存在
maxNum = int(input("请输入检测范围的最大值:maxNum="))
num1 = int(input("请输入加上的第一个数:num1="))
num2 = int(input("请输入加上的第二个数:num2="))
lt=[]
def check(num):
    flag = False
    for i in range(num):
        if i == math.sqrt(num):
            flag = True
            return flag
        else:
            flag = False
    return flag
#函数功能：maxNum进行遍历,并将找到的完全平方数存到列表lt中。
def get(maxNum):
    for i in range(maxNum):
        if check(i+num1) and check(i+num1+num2):
            lt.append(i)
        else:
            # print("这个数不存在")
            pass
get(maxNum)
print(lt)





