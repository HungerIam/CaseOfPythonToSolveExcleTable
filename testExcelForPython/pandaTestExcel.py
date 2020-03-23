
# coding: utf-8
import  pandas  as pd
 
 
# 1. 读取前n行所有数据
 
df = pd.read_excel('testForPython1.xlsx')#读取xlsx中第一个sheet
data1 = df.head(7)   # 读取前7行的所有数据，dataFrame结构
data2 = df.values    #list形式，读取表格所有数据
print("获取到所有的值:\n{0}".format(data1)) #格式化输出
print("获取到所有的值:\n{0}".format(data2)) #格式化输出
