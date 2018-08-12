# coding: utf-8

import requests
import execjs
import re

headers = {
        'Accept': 'text/html, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.cnvd.org.cn',
        'Referer': 'http://www.cnvd.org.cn/flaw/typelist?typeId=29',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'X-Requested-With': 'XMLHttpRequest',
}

# 发出请求开始计算 cookies
resp = requests.get('http://www.cnvd.org.cn/flaw/list.htm', headers=headers)
body = resp.text
print body
# 清楚无用字符
rep = re.compile("</?script>|\x00|\r|\n")
# 处理返回 JavaScript 脚本
js = "function get_ck(){"+rep.sub('',body.encode('utf-8').replace("eval", "return"))+'}'
print js
# 执行脚本 
get_ck = execjs.compile(js).call("get_ck")
# print '*'
print get_ck
# 处理执行结果，提取有用信息
dc_cookie = re.search("\{while\(.*?\)\{\};(.*?)set.*cookie=\(dc\+\'(.*?)\'\).*\}$", get_ck)
dc = dc_cookie.group(1)
cookie = "function cookie(){"+dc+"return dc}"
cookies = execjs.compile(cookie).call("cookie")# + dc_cookie.group(2)
cookie_list = cookies.encode('utf8').strip(';').split(';')
cookie_dict = dict(resp.cookies)
for cookie in cookie_list:
    kv = cookie.split('=')
    cookie_dict[kv[0]] = kv[1]

resp = requests.get('http://www.cnvd.org.cn/flaw/typeResult?typeId=29&max=20&offset=20', headers=headers, cookies=cookie_dict)
print resp.text