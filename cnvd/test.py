# -*- coding:utf-8 -*-

import requests
from splinter import Browser
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_cookie(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    sleep(3)
    tmp = driver.get_cookies()
    cookie=''
    for c in tmp:
        cookie += c['name'] +'='  +  c['value'] +';'
        
    driver.quit()
    print cookie


#get_cookie("http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=20&typeId=29")

def splinter(url):
    browser = Browser('chrome', headless=True, user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    browser.visit(url)
    sleep(3)
    tmp = browser.cookies.all()
    print tmp
    cookie=''
    for key in tmp:
        cookie += str(key) +'=' + tmp[key] +';'
        
    browser.quit()
    return cookie

#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/65.0.3325.181 Safari/537.36"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
headers["Cookie"] = splinter("http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=20&typeId=29")
res=requests.get("http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=20&typeId=29",headers=headers,timeout=5)
print res.text