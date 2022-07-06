import requests
import execjs
with open("../2.js",'r',encoding='utf-8') as f:
    JSData = f.read()
base_url = "https://match.yuanrenxue.com/api/match/2?page={page}"
m = execjs.compile(JSData).call('get_m_value')
headers = {
    "referer": "https://match.yuanrenxue.com/match/1",
    'User-Agent': 'yuanrenxue.project',
    "cookie":f"sessionid=3q5vpbacgldqlt0t8dfv8nykv8zk7ili;m={m}"
}
res = 0
for i in range(1,6):

    response = requests.get(base_url.format(page=i),headers=headers).json()
    print(response)
    for val in response['data']:
        res += val['value']
print(res)