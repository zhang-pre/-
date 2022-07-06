import pywasm
import execjs
import requests
with open("../15.js",'r',encoding='utf-8') as f:
    JSData = f.read()

runtime = pywasm.load('../main.wasm')
base_url = "https://match.yuanrenxue.com/api/match/15?m={m}&page={page}"
headers = {
    "referer": "https://match.yuanrenxue.com/match/15",
    'User-Agent': 'yuanrenxue.project',
    "cookie": "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1654782538; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1654741841,1654745736,1654778137,1654828136; no-alert3=true; tk=-392251687480763807; sessionid=2fzxfzeoc3j24gi1djeryd2iilxqazbj;Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1654741894,1654745752,1654778176,1654844774; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1654846225; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1654846274"
}
res = 0
for i in range(1,6):
    value = execjs.compile(JSData).call('get_value')
    result = runtime.exec('encode', [value[0], value[1]])
    token =str(result) + '|' + str(value[0])+ '|' + str(value[1]);
    url = base_url.format(page=i, m=token)
    response = requests.get(url,headers=headers).json()
    for val in response['data']:
        res += val['value']
print(res)
