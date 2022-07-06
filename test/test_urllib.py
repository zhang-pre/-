import urllib.error  # 制定URL,获取网页数据
import urllib.request
import urllib.parse

''' 第一步，先封装request对象，让request请求更像是一个浏览器发出的
    第二步，发送request请求，接收response响应对象，可能需要用decode('utf-8')方法进行解码
    第三步，解析数据

# 见名知意 在urllib包中，request是一个request请求，urlopen是访问一个url地址
# 对于urllib.request.urlopen('http://www.baidu.com')返回的response对象，还可以获取到很多信息，如response.getheaders(),response.status()等等
# get请求
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

# post请求
pro_data = {'hello': 'world'}
data = bytes(urllib.parse.urlencode(pro_data), encoding="utf-8")
# 为什么要传输数据，因为当进行post形式访问时，不能够用http://httpbin.org/post这种方式直接访问，需要传递一些post的表单信息
# 通过对post表单信息的封装，才能够进行post形式的访问。
# urllib.parse解析器
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))


# 超时处理
# 若超时了，则直接放弃爬取，先爬取别的
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print('timeout')
    '''

# 封装request对象
url = "https://movie.douban.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 "}
req = urllib.request.Request(url=url, headers=headers)  # 封装request对象
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

