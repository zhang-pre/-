import execjs
import requests

with open('window.js','r') as f:
    JSDate = f.read()
JS = execjs.compile(JSDate)
arr = JS.call("get_my_value")
print(arr)
data = {
    "end": "2022-07-01",
    "rank_name": "文化",
    "rank_name_group": "生活",
    "start": "2022-07-01",
    "nonce": arr[0],
    "xyz": arr[1]
}
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
res = requests.post("https://www.newrank.cn/xdnphb/main/v1/day/rank",data=data,headers=headers)
print(res.text)