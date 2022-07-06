import requests
import execjs
import re

# 多了个yuanrenxue的cookie
# url = "https://match.yuanrenxue.com/api/match/13"
headers = {
    "referer": "https://match.yuanrenxue.com/match/13",
    'User-Agent': 'yuanrenxue.project',
    "cookie": "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1654782538; sessionid=9teoml72wkb9kob9ddku9peb8dgu7p2i; qpfccr=true; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1654828136,1654850658,1654853324,1654862597; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1654745752,1654778176,1654844774,1654862632; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1654862632;Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1654865249;"
}
# str.replace('|','%E4%B8%A8')
url = "https://match.yuanrenxue.com/match/13"
res = requests.get(url, headers=headers)
reg = re.compile("'([a-zA-Z0-9=|_])'")
results = reg.findall(res.text)
cookie = ''.join(results)
key, value = cookie.split('=')
headers["cookie"] = headers["cookie"] + cookie
detail_url = "https://match.yuanrenxue.com/api/match/13?page={page}"
# https://match.yuanrenxue.com/api/match/13?page=1
ans = 0
for i in range(1, 6):
    res = requests.get(detail_url.format(page=i), headers=headers).json()
    for t in res['data']:
        ans += t['value']
print(ans)
