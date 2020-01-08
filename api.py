from selenium import webdriver
from bs4 import BeautifulSoup
import time, urllib.request, requests, json, csv, random, os
from selenium.webdriver import ChromeOptions
import cx_Oracle as oci

open_api = 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=%s&y=%s&input_coord=WGS84'%(129.087635632412,35.251023107627)
api_key = 'f56b92905ade194d1254314f9e91d103'

res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
dic1 = res.json()

result = dic1['documents'][0]['address']['address_name']

print(result)