import pandas as pd
import cx_Oracle as oci
import matplotlib.pyplot as plt

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()


sql = 'SELECT * FROM TAXI'
cursor.execute(sql)
data = cursor.fetchall()

df = pd.DataFrame(data)


df.columns = ['No','기준년월일','요일','시간대','발신지_시도','발신지_시군구','발신지_읍면동','통화건수']

# print(df.head())

df_table = df.pivot_table('통화건수',columns='발신지_시군구',index='기준년월일',aggfunc='sum')

print(df_table)

plt.plot(df_table)
# plt.show()