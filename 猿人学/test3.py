import requests
session = requests.session()
class Headers(object):
    def items(self):
        return (
            ("Host", "match.yuanrenxue.com"),
            ("Connection", "keep-alive"),
            ("Content-Length", "0"),
            ("sec-ch-ua", '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"'),
            ("sec-ch-ua-mobile", "?0"),
            ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"),
            ("sec-ch-ua-platform", '"Windows"'),
            ("Accept", "*/*"),
            ("Origin", "https://match.yuanrenxue.com"),
            ("Sec-Fetch-Site", "same-origin"),
            ("Sec-Fetch-Mode", "cors"),
            ("Sec-Fetch-Dest", "empty"),
            ("Referer", "https://match.yuanrenxue.com/match/3"),
            ("Accept-Encoding", "gzip, deflate, br"),
            ("Accept-Language", "zh-CN,zh;q=0.9"),
        )
session.headers = Headers()

jssm_url ="https://match.yuanrenxue.com/jssm" # post
res1 = session.post(jssm_url)
print(res1.status_code)
print(res1.cookies)
# url = "https://match.yuanrenxue.com/api/match/3"
# res2 = session.get(url)
# print(res2.status_code)
