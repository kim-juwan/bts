from selenium import webdriver
from bs4 import BeautifulSoup
import time, urllib.request, requests, json, csv, random, os
from selenium.webdriver import ChromeOptions
import cx_Oracle as oci
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()

select_sql = 'SELECT (BUSTOPID,X,Y) FROM BUS'
cursor.execute(select_sql)
xys = cursor.fetchall()

for xy in xys:
    bustop = xy[0]
    x = xy[1]
    y = xy[2]
    open_api = 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=%s&y=%s&input_coord=WGS84'%(x,y)
    api_key = 'f56b92905ade194d1254314f9e91d103'

    res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
    dic1 = res.json()

    result = dic1['documents'][0]['address']['address_name']

    print(result)

    update_sql = 'UPDATE BUS SET 시군구=:1, 읍면동=:2 WHERE BUSTOPID=:3'
    cursor.execute(sql,data)
    conn.commit()