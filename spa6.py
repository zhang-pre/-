import requests
import execjs
with open("test2.js",'r',encoding='utf-8') as f:
    JSData = f.read()
JS = execjs.compile(JSData)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
base_url = "https://spa6.scrape.center/api/movie/?limit={limit}&offset={offset}&token={token}"
# offset从0开始，limit保持不变
offset = 0
while(offset<=10):
    token = JS.call('get_my_value')
    url = base_url.format(limit=10,offset=offset,token=token)
    res = requests.get(url,headers=header).json()
    offset+=10
    detail_url = "https://spa6.scrape.center/api/movie/{t}/?token={token1}"
    m = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
    for result in res['results']:
        t = JS.call('base',[m+str(result["id"])])
        token1 = JS.call('get_my_value')
        detail_res = requests.get(url.format(t=t,token1=token1),headers=header)
        print(detail_res.text)


# 再进行base64编码，就能得到了
# 如果不对的话，就把引号去掉