import re

import execjs
import requests
import config

def get_hot_list(page):
    with open('../5.js', 'r', encoding='utf8') as f:
        ctx = execjs.compile(f.read())
    result = ctx.call('get_params')
    url_m,url_f,m,RM4h = result['url_m'],result['url_f'],result['m'],result['RM4hZBv0dDon443M']
    url = 'https://match.yuanrenxue.com/api/match/5'
    params = {
        'page': page,
        'm': url_m,
        'f': url_m
    }
    headers = {
        "referer": "https://match.yuanrenxue.com/match/1",
        'User-Agent': 'yuanrenxue.project',
        "cookie": f'm={m};RM4hZBv0dDon443M={RM4h};sessionid=nc9t6ov4dbgm3hsv31aiwrjjf4e4g2jl'
    }
    res = requests.get(url=url, headers=headers, params=params)
    data = [item['value'] for item in res.json()['data']]
    print(data)
    return data


if __name__ == '__main__':
    hot_list = []
    for i in range(1, 6):
        hot_list.extend(get_hot_list(i))

    hot_list.sort(reverse=True)
    print(hot_list)
    print(sum(hot_list[:5]))





