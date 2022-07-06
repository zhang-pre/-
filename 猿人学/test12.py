import requests
import execjs

headers = {
    "referer": "https://match.yuanrenxue.com/match/12",
    'User-Agent': 'yuanrenxue.project',
    "cookie": "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1654782538; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1654741841,1654745736,1654778137,1654828136; no-alert3=true; tk=-392251687480763807; sessionid=9teoml72wkb9kob9ddku9peb8dgu7p2i; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1654741894,1654745752,1654778176,1654844774; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1654846225; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1654846274"
}
url = "https://match.yuanrenxue.com/api/match/12?page={page}&m={token}"
res = 0
for i in range(1,6):
    token = execjs.eval(f"btoa('yuanrenxue' + {i})")
    # token = token.replace('=', '%3D')
    response = requests.get(url.format(page=i, token=token),headers=headers).json()
    for val in response['data']:
        res += val['value']
print(res)
