import requests
import execjs
with open("../16.js",'r',encoding='utf-8') as f:
    JSData = f.read()
# 投毒的定义：投毒，指的是js代码中会对环境进行很多检测，如果识别为非正常浏览器，就会对某些参数进行修改，造成最终结果错误，这种过程称为投毒。
# 常见的投毒位置
    # try ...cach...
    # if ... else...
    # 判断表达式： | | 或 & & 或 ?
# 插桩定位
# 在本地 js 文件可能投毒的位置，使用 console.log 打印出值；
# 在浏览器相同位置打上断点，查看运行的结果值；
# 进而对比二者是否相同，如果不同就是此处被投毒了。
headers = {
    "referer": "https://match.yuanrenxue.com/match/16",
    'User-Agent': 'yuanrenxue.project',
    "cookie": "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1654782538; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1654741841,1654745736,1654778137,1654828136; no-alert3=true; tk=-392251687480763807; sessionid=xfxnd3w878jthsux6xsxhowxfo70ep3s;Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1654741894,1654745752,1654778176,1654844774; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1654846225; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1654846274"
}
url = "https://match.yuanrenxue.com/api/match/16?page={page}&m={m}&t={t}"



res = 0
for i in range(1,6):
    array = execjs.compile(JSData).call('diaoyong1')
    response = requests.get(url.format(page=i, m=array[1],t=array[0]),headers=headers).json()
    print(response)
    # for val in response['data']:
    #     res += val['value']
print(res)
