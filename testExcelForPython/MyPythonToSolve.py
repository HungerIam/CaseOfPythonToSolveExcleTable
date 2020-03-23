#引入依赖包
import xlsxwriter
import xlrd

book1 = xlrd.open_workbook('table1.xlsx')
book2 = xlrd.open_workbook('table2.xlsx')

sheet1 = book1.sheets()[0]
sheet2 = book2.sheets()[0]

sheet1_nrows = sheet1.nrows

print('表格1总行数',sheet1_nrows)

sheet2_col1_values = sheet2.col_values(0,1,3)

print('表格2第1列值',sheet2_col1_values)

#创建一个新的Excel文档
myExcel = xlsxwriter.Workbook('table3.xlsx')
#添加一个工作表
myWorkSheet = myExcel.add_worksheet()
#设置行和列的偏移
row,col = 0,0
#设置循环中的参数
i = 0
while i<sheet1_nrows:	
	if sheet1.cell(i,0).value not in sheet2_col1_values:
		#制定行、列的单元格，添加数据

		myWorkSheet.write(row,col,sheet1.cell(i,0).value)
		myWorkSheet.write(row,col+1,sheet1.cell(i,1).value)
		#行增加
		row+=1
	i+=1	
#关闭文档
myExcel.close()


