#导入随机数
import random
import time

num=random.randint(0,10)
#随机输入0到10的正数比较大小；
num1=int(input("请输入一个0-10的数："))

if num1>num:
    print("大")
elif num1<num:
    print("小")
elif num1==num:
    print("和")
print(num)
    # tim=time.sleep(3)
    # print("间隔3miaohou显示",tim)





