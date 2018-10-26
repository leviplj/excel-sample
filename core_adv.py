from functools import partial
from openpyxl import load_workbook

wb = load_workbook(filename='sample.xlsx')

work_sheet = wb['Sheet1']

get_cell = lambda x, y: '{}{}'.format(x,y)
get_value = lambda x, y: work_sheet[get_cell(x, y)].value

get_name = lambda x: get_value('B', x)
get_gender = lambda x: get_value('D', x) 
get_age = partial(get_value, 'F')        #Isso é praticamente a mesma coisa da linha de cima
                                         #só fiz assim p mostrar uma forma diferente de fazer

males = []
females = []

row = 2
while True:
    name = get_name(row)
    gender = get_gender(row)
    age = get_age(row)

    print(name, gender, age)

    if not name:
        break

    if gender == 'Male':
        males.append({'name': name, 'age': age})
    else:
        females.append({'name': name, 'age': age})

    row = row + 1

print(males)

work_sheet[get_cell('C', row)] = 'Qtd. male'
work_sheet[get_cell('D', row)] = len(males)
work_sheet[get_cell('E', row)] = 'Qtd. female'
work_sheet[get_cell('F', row)] = len(females)

wb.save(filename='sample2.xlsx')