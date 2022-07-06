import requests
import execjs
with open("../副1.js",'r',encoding='utf-8') as f:
    JSData = f.read()
base_url = "https://match.yuanrenxue.com/api/match/1?page={page}&m={token}"
headers = {
    "referer": "https://match.yuanrenxue.com/match/1",
    'User-Agent': 'yuanrenxue.project',
}
res = 0
for i in range(1,6):
    token = execjs.compile(JSData).call('get_m_value')
    print(token)
    url = base_url.format(page=i, token=token).replace('丨','%E4%B8%A8')
    response = requests.get(url,headers=headers).json()
    for val in response['data']:
        res += val['value']
print(res/50)