import re

from bs4 import BeautifulSoup

'''
BeautifulSoup4主要的功能是如何解析和提取 HTML/XML 数据。
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
所有对象可以归纳为4种:
        Tag
        NavigableString
        BeautifulSoup
        Comment
'''
file = open("./baidu.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")  # 有一个BeautifulSoup对象，帮助解析文档,使用html解析器，得到文件的树形结构
'''
print(bs.title)  # 1.Tag 标签及其内容：拿到它所找到的第一个内容
print(bs.title.string)  # 2.NavigableString 标签里的内容（字符串）
print(bs.a.attrs)  # 拿到标签中所有的属性，并返回一个字典
print(bs)  # 3.BeautifulSoup,表示整个文档
print(bs.a.string)  # 3.Comment  是一个特殊的NavigableString，输出的内容不包括注释符号
'''

# 文档的遍历
# print(bs.head.contents) #返回一个list

# 文档的搜索
#  1
# (1) find_all()
# 字符串过滤，会查找标签与字符串完全匹配的内容
# t_list = bs.find_all('a')  # 只会查找a标签以及内容

# (2)使用正则表达式来匹配内容  最主要
# t_list = bs.find_all(re.compile('a'))  # 包含字母a的标签就会与其内容一起被显示出来，如<head>,<meta>

#  (3)传入一个函数（方法），根据函数的要求来搜索
'''
def name_is_exist(tag):
    return tag.has_attr("name")  # 返回有name的标签


t_list = bs.find_all(name_is_exist)
# find_all()方法会将html中每个标签作为参数传入到name_is_exist，所以该方法不需要传参数，连()都不要
for item in t_list:
    print(item)
'''

# 2.kwargs  keyword参数
# t_list = bs.find_all(id='head')
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# 3.text参数
# t_list = bs.find_all(text=["hao123", "地图"])
# t_list = bs.find_all(text=re.compile("\d")) #应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)

# 在find_all()函数中加limit=xx ,指明得到结果个数小于等于xx个

# 4.css选择器
# t_list = bs.select('title')   #通过标签来查找
# t_list = bs.select(".mnav")     #通过类名来查找
# t_list = bs.select("#u1")   #通过id来查找
# t_list = bs.select("a[class='bri']")  #通过属性来查找
# t_list = bs.select("head > title")  #通过子标签来查找
t_list = bs.select(".mnav ~ .bri")

print(t_list[0].get_text())

# for item in t_list:
#     print(item)
