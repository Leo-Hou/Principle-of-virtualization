import requests
 
conn = requests.session()
url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LIcAc'
postdata = {
    'username':'zhaoxn04',
    'password':'wobugaosuni2004'
}
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
rep = conn.post(url, data=postdata,headers=headers)
with open('1.html', 'wb') as f:
    f.write(rep.content)
 
url1 = 'http://bbs.chinaunix.net/thread-4246512-1-1.html'
rep1 = conn.get(url1, headers=headers)
with open('2.html', 'wb') as f:
    f.write(rep1.content)
