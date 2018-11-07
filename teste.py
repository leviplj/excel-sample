import requests
import datetime
url_login = 'https://www.motortax.ie/OMT/login.do'

url_change_email = 'https://www.motortax.ie/OMT/changeEmail.do'

url_insurance = 'https://www.motortax.ie/OMT/insurance.do'

url_tax = 'https://www.motortax.ie/OMT/tax.do'

def end_date_valid(date):
    in_six_months = datetime.datetime.now() + datetime.timedelta(6*30)

    return date > in_six_months

####
if datetime.datetime.now().month < 7:
    expYear = datetime.datetime.now().year
else:
    expYear = datetime.datetime.now().year + 1
    
for customer in Road_Tax:
    if customer['ins_months'] == '12 months':
        mtSelectedLicence = 2

    elif customer['ins_months'] == '6 months':
        mtSelectedLicence = 1

    elif customer['ins_months'] == '3 months':
        mtSelectedLicence = 0
    
    else:
        mtSelectedLicence = None

## em cada linha 0 = 3 months, 1 = 6 monhts, 2 = 12 months

dataframe = [
    {'loginRegNo': '152D22519', 'loginPin': '790206',
     'ownerEmail': 'donotreply@sixtleasing.ie', 'ownerEmailConfirm': 'donotreply@sixtleasing.ie',
     'insCompany': 'ZU', 'insExpiryDay': '01', 'insExpiryMonth': '07', 
        'insExpiryYear': f'{expYear}', 'insPolicyNumber': '01Amv0590380/A', 'mtSelectedLicence': '', 'solved': 'S'},

    {'loginRegNo': '152D22519', 'loginPin': '790206',
     'ownerEmail': 'donotreply@sixtleasing.ie', 'ownerEmailConfirm': 'donotreply@sixtleasing.ie',
     'insCompany': 'ZU', 'insExpiryDay': '01', 'insExpiryMonth': '07', 
        'insExpiryYear': f'{expYear}', 'insPolicyNumber': '01Amv0590380/A', 'mtSelectedLicence': '', 'solved': 'N'},
]


errors = []

for line in dataframe:
    if line['mSelectedInsurance'] == None:
        errors.append({'customer': line, 'description': 'Insurance not selected'})

    elif not end_date_valid(line['End Date']):
        errors.append({'loginRegNo': line['loginRegNo'], 'description': 'Expire date too close'})       

    else:
        log.add('loginRegNo')
        data_login = {'loginRegNo': line['loginRegNo'], 'loginPin': line['loginPin']}

        r = requests.post(url_login, data=data_login)

        if line['ownerEmail'] not in r.content:
            data_owner_email = {'ownerEmail': line['ownerEmail'], 
                'ownerEmailConfirm': line['ownerEmailConfirm']}

            r = requests.post(url_change_email, data=data_owner_email)

        data_insurance = {'insCompany': line['insCompany'], 'insExpiryDay': line['insExpiryDay'],
            'insExpiryMonth': line['insExpiryMonth'], 'insExpiryYear': line['insExpiryYear'], 
            'insPolicyNumber': line['insPolicyNumber']
        }

        r = requests.post(url_insurance, data=data_insurance)


        data_tax = {'mSelectedInsurance': line['mSelectedInsurance']}

        r = requests.post(url_tax, data=data_tax)

        ###
        #processamento do pagamento
# fim do loop

cria_pdf_envia_por_email(errors)

print(errors)

    


    
    


"""


values = {'loginRegNo': '152D22519',
          'loginPin': '790206'}

r = requests.post(url, data=values)
print(r.content)"""