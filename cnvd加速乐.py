import requests
import execjs
import re
with open('cnvd加速乐.js', 'r', encoding='utf-8') as f1:
    JSData1 = f1.read()
with open('cnvd加速乐2.js', 'r', encoding='utf-8') as f2:
    JSData2 = f2.read()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "Host": "www.cnvd.org.cn",
    "Referer": "https://www.cnvd.org.cn/flaw/typelist?typeId=29"
}
session = requests.Session()
jar = requests.cookies.RequestsCookieJar()
session.headers = headers
typelist_url = "https://www.cnvd.org.cn/flaw/typelist?typeId=29"
favico_url = "https://www.cnvd.org.cn/favicon.ico"
res1 = session.get(typelist_url)
session.cookies = res1.cookies
for cookie in session.cookies:
    jar.set(cookie.name,cookie.value)
cookie = re.search('<script>document.cookie=(.*?);location',res1.text).group(1)
x = execjs.eval(cookie).split(';')[0].split('=')
session.cookies[x[0]] = x[1]
jar.set(x[0],x[1])
# cookie1 = res1.cookies
cookie2 = execjs.compile(JSData1).call('get_cookie')
cookie3 = execjs.compile(JSData2).call('get_cookie')
result1 = re.match('__jsl_clearance_s=(.*?);',cookie2)
jar.set('__jsl_clearance_s',result1.group(1))
result2 = re.match('__jsl_clearance_s=(.*?);',cookie3)
jar.set('__jsl_clearance_s',result2.group(1))
print(jar)
res2 = session.get(typelist_url,cookies=jar)
print(res2.text)
