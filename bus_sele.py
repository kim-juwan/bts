from selenium import webdriver
from selenium.webdriver import ChromeOptions
import cx_Oracle as oci
from bs4 import BeautifulSoup
import time, urllib.request
import requests

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #브라우저 안 보임
chrome_options.add_argument('disable-gpu') # 가속 사용 x
chrome_options.add_argument('lang=ko_KR') # 가짜 플러그인 탑재


# id_sql = 'SELECT ID FROM REST'
# cursor.execute(id_sql)
# rows = cursor.fetchall()

driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
url = 'http://bus.busan.go.kr/busanBIMS/bus_map/map_main.asp?menuNum=2&amp;mapGubun=undefined'

driver.get(url)
time.sleep(2) #데이터 뜰때까지 기다려주는 시간

driver.find_element_by_xpath('//*[@id="key"]').send_keys('96-1')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="dlBus"]/dd[2]/button/img').click()
# url2 = driver.current_url
# # driver.get(url2)
time.sleep(2)   
driver.find_element_by_css_selector('body > div > div:nth-child(1) > p.btmore > a:nth-child(2) > img').click()
