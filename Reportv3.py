import requests,uuid,secrets
import sys
import time
import os
import colorama

os.system('pip install requests')
os.system('pip install colorama')
os.system('pip install os')
os.system('pip install time')
os.system('pip install secrets')
os.system('pip install uuid')
os.system('pip install sys')
os.system('pip install pyfiglet')
os.system('clear')

Z = '\x1b[2;31m'
X = '\x1b[2;36m'
G = '\x1b[1;32m'
E = '\x1b[1;34m'
S = '\x1b[1;33m'

def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.030)

j(Z+ '    ____       _      _          _      __  __   \n')
j(G+ '   / ___|     / \    | |        / \    |  \/  | \n')
j(Z+ '   \___ \    / _ \   | |       / _ \   | |\/| |  \n')
j(G+ '    ___) |  / ___ \  | |___   / ___ \  | |  | | \n')
j(Z+ '   |____/  /_/   \_\ |_____| /_/   \_\ |_|  |_|')        
        
j(Z+ '\n    _   _   _   _   _   _   _____   _____   ____\n')
j(G+ '   | | | | | | | | | \ | | |_   _| | ____| |  _ \ \n')
j(Z+ '   | |_| | | | | | |  \| |   | |   |  _|   | |_) | \n')
j(G+ '   |  _  | | |_| | | |\  |   | |   | |___  |  _ <\n')
j(Z+ '   |_| |_|  \___/  |_| \_|   |_|   |_____| |_| \_\ \n')

j('_______________________________________________________________\n')
j(G + '\n  « BoT RePorT SelF » \n')
j(Z+ '\n ♡ CreaDed By SaLaM HunTer ♡     \n')
j(G+ '\n  InstaGram = @salamamzori \n')
j(E+ '\n  TeleGram = @salammzori \n')
j(X+ '\n  ChanneL = @T5B55 \n')
j('\n_______________________________________________________________\n')

from time import sleep
uid = uuid.uuid4()
 
r = requests.Session()
cookie = secrets.token_hex(1)*0
username = input(Z+ '\n  [+] Username Instagram : ')
password = input(Z+ '  [+] Password Instagram : ')
target = input(Z + '  [+] Enter Target : ')
sle = int(input(Z + '  [+] Enter Sleep : '))
much = int(input(Z + '  [+] How many report : '))
def login():
    global username
    global password
    
    url = 'https://www.instagram.com/accounts/login/ajax/'
    
    headers = {"user-agent": 'Mozilla/5.0 (Linux; Android 9; SM-A10S5F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print(G + '  Login Successfully')
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            for i in range(much):
             url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'profile','reason_id':1,'frx_context':''}
            report = r.post(url_report,data=datas)
            print('  Done Self = {}'.format(done))
            sleep(sle)
            done += 1


    else:
        print(E + '  Error Login ! ')
        exit()
 

#SALAM HUNTER
login()

