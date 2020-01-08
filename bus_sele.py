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


# # id_sql = 'SELECT ID FROM REST'
# # cursor.execute(id_sql)
# # rows = cursor.fetchall()

# driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
# url = 'http://bus.busan.go.kr/busanBIMS/bus_map/map_main2.asp?menuNum=4&mapGubun=daum'

# driver.get(url)
# time.sleep(4) #데이터 뜰때까지 기다려주는 시간

# driver.find_element_by_xpath('//*[@id="txtLineNum"]').send_keys('96-1')

# time.sleep(1)

# driver.find_element_by_xpath('//*[@id="am_topm2_5"]/ul/li[5]/button/img').click()
# url1 = driver.current_url
# html = requests.get(url1)
# soup = BeautifulSoup(html.content,'lxml')
# print(soup)

url = 'http://121.174.75.24/bims_web/popup2/RealTimeBus.aspx?BNUM=96-1'

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'lxml')

print(soup)