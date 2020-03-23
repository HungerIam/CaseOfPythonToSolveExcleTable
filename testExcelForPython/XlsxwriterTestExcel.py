#引入依赖包
import xlsxwriter

#贮备数据
datas = (['参加过会议人数',1],['没参加会议人数',2])

#开始操作
#创建一个Excel文档
myExcel = xlsxwriter.Workbook('testCreateExcel.xlsx')
#添加一个工作表
myWorkSheet = myExcel.add_worksheet()

#设置行和列的偏移
row,col = 0,0

#开始添加数据
for  item,cost in datas:
	#制定行、列的单元格，添加数据
	myWorkSheet.write(row,col,item)
	myWorkSheet.write(row,col+1,cost)
	#行增加
	row+=1

#添加一个计算总数的函数
myWorkSheet.write(row,0,'总人数')
myWorkSheet.write(row,1,'=SUM(B1:B2)')

#关闭文档
myExcel.close()