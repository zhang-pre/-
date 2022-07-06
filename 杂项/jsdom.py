import execjs
with open('./jsdom.js','r',encoding='utf-8') as f:
    js = f.read()
# t = execjs.compile(js,cwd="../node_modules/jsdom").call("sign")
t = execjs.compile(js).call("sign")
print(t)