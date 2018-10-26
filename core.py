from openpyxl import load_workbook

wb = load_workbook(filename='sample.xlsx')

work_sheet = wb['Sheet1']

males = []
females = []

row = 2
while True:
    name = work_sheet['B{}'.format(row)].value
    gender = work_sheet['D{}'.format(row)].value
    age = work_sheet['F{}'.format(row)].value

    print(name, gender, age)

    if not name:
        break

    if gender == 'Male':
        males.append({'name': name, 'age': age})
    else:
        females.append({'name': name, 'age': age})

    row = row + 1

# processa os dados como quiser aqui

work_sheet['C{}'.format(row)] = 'Qtd. male'
work_sheet['D{}'.format(row)] = len(males)
work_sheet['E{}'.format(row)] = 'Qtd. female'
work_sheet['F{}'.format(row)] = len(females)

wb.save(filename='sample2.xlsx')