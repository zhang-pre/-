# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则
import urllib.request, urllib.error  # 制定URL,获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getDate(baseurl)
    savaPath = "豆瓣电影Top250.xls"
    # 3.保存数据
    saveData(datalist, savaPath)


# 爬取电影名称，豆瓣评分，评价数，电影概况，电影链接
findName = re.compile(r'<span class="title">(.*?)</span>')
findLink = re.compile(r'<a href="(.*?)">')
findDoubanGrade = re.compile(r'<span class="rating_num" property="v:average">([0-9.]*)</span>')
findEvaluateNumber = re.compile(r'<span>([0-9]+)人评价</span>')


# 加括号的威力，让它成一个组
# 爬取网页
def getDate(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")  # 有一个BeautifulSoup对象，帮助解析文档,使用html解析器，得到文件的树形结构
        for item in soup.find_all("div", class_="item"):
            data = []
            item = str(item)  # item是bs类型的，要用它来使用正则，需要转换成string型的
            '''item.select(".hd > a > span:first-of-type")[0].get_text()
            item.select(".hd > a > span:nth-child(2)")[0].get_text() 
            除了用正则，还可以用bs4的方法来获取相应的内容
            注意：用bs4的话要确保item也是BeautifulSoup类型，所以item不要转换成字符串
            '''
            name = re.findall(findName, item)
            data.append(name[0])
            if len(name) >= 2:
                oname = name[1].replace(u'\xa0', '')  # 完美去除\xa0，其实就是空格
                # 字符串前加u，解决中文乱码问题，后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面
                data.append(oname.replace('/', ''))
            else:
                data.append("")
            data.append(re.findall(findLink, item)[0])  # 链接
            data.append(re.findall(findDoubanGrade, item)[0] + "分")  # 豆瓣评分
            data.append(re.findall(findEvaluateNumber, item)[0] + "人评价")
            datalist.append(data)
    return datalist


# 得到指定的一个URL的网页内容
def askURL(url):
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 "}
    html = ""
    request = urllib.request.Request(url=url, headers=header)  # 封装request对象
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        #  看下如果发生异常，返回什么类型的code
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def saveData(datalist, savaPath):
    workbook = xlwt.Workbook(encoding="utf-8")
    sheet = workbook.add_sheet(sheetname="sheet1", cell_overwrite_ok=True)
    index = ['中文名', '英文名', '链接', '豆瓣评分', '评价人数']
    for i in range(len(index)):
        sheet.write(0, i, index[i])
    # datalist列表中有250个列表，每个子列表中有5个元素
    for i in range(len(datalist)):
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i+1, j, data[j])
    workbook.save(savaPath)
if __name__ == '__main__':
    main()
