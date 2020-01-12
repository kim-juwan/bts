from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import pandas as pd
import folium
import json
from folium.features import DivIcon
import cx_Oracle as oci
import matplotlib.pyplot as plt


def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def index2(request):
    
    return render(request,'index2.html')
def busanmap(request):
    conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
    cursor = conn.cursor()

    sql = 'SELECT * FROM TAXI'
    cursor.execute(sql)
    data = cursor.fetchall()

    df = pd.DataFrame(data)

    df.columns = ['No','기준년월일','요일','시간대','발신지_시도','발신지_시군구','발신지_읍면동','통화건수']
    tel = df.groupby('발신지_시군구').sum()['통화건수']
    df_gu = pd.read_sql_query('SELECT * FROM BUSAN',conn)
    file_path = 'static/부산광역시_전체_세대_및_인구개황_20200108153737.csv'
    df = pd.read_csv(file_path,encoding='euc-kr')
    df = df.set_index('구·군별')
    df = df.iloc[1:,[2]]
    geo_path='static/busan.json'
    
    try:
        geo_data = json.load(open(geo_path,encoding='utf-8'))
    except:
        geo_data = json.load(open(geo_path,encoding='utf-8-sig'))
        
    g_map = folium.Map(location=[35.1831154,129.0710543],tiles='Stamen Terrain',zoom_start=11)


    folium.Choropleth(geo_data=geo_data,data=df['인구수'],columns=[df.index,df['인구수']],fill_color='YlOrRd',fill_opacity=0.5,line_opacity=1,line_color='white',line_weight=2,key_on='feature.properties.SIG_KOR_NM',threshold_scale=[40000,150000,250000,350000,450000]).add_to(g_map)
    for row in range(len(df_gu)):
        folium.map.Marker([df_gu.iloc[row,0], df_gu.iloc[row,1]-0.01],icon=DivIcon(icon_size=(150,36),icon_anchor=(0,0),html='<div style="font-family:BMDO;font-size: 10pt;color:#000000">%s<br/>%s</div>' %( df_gu.iloc[row,2],tel[ df_gu.iloc[row,2]   ]),)).add_to(g_map)
    g_map.save('.templates/busan.html')

    return render(request,'busan.html',{'g_map':g_map})