import openpyxl
from docxtpl import DocxTemplate, R
 
wb = openpyxl.load_workbook('D.xlsx')

sheets = wb.active
data = []
for row in sheets.iter_rows(values_only=True):
    temp=[]
    for cell in row:
        temp.append(cell)
    data.append(temp)

wb.close()
del data[0]

doc = DocxTemplate('1.docx')

context = {
    'items':data,
    "page_break":R("\f")
}
doc.render(context)

doc.save('Дипломники.docx')