import httpx
data = {
    "username":"1301673843",
    "password":"zl1301673843"
}
headers = {
    "referer": "https://match.yuanrenxue.com/match/17",
    'User-Agent': 'yuanrenxue.project',
}
client = httpx.Client(http2=True)

# session = requests.Session()
res = client.post("https://match.yuanrenxue.com/api/login",data=data)
print(res.cookies)
cookies = res.cookies
ans = 0
for i in range(1,6):
    res2 = client.get(f"https://match.yuanrenxue.com/api/match/17?page={i}",cookies=cookies,headers=headers).json()
    print(res2)
    for t in res2['data']:
        ans += t['value']
print(ans)
