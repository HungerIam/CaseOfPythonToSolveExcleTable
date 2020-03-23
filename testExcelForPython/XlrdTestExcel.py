import xlrd

book = xlrd.open_workbook('table1.xlsx')

sheet1 = book.sheets()[0]

nrows = sheet1.nrows

print('表格总行数',nrows)

ncols = sheet1.ncols

print('表格总列数',ncols)

row3_values = sheet1.row_values(2)

print('第3行值',row3_values)

col2_values = sheet1.col_values(1)

print('第2列值',col2_values)

cell_3_2 = sheet1.cell(2,1).value

print('第3行第2列的单元格的值：',cell_3_2)

all = sheet1.get_rows()

print('表单的值为：',all)

