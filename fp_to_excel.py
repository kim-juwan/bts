import cx_Oracle as oci
import pandas as pd 

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')

df = pd.read_sql_query("select * from bus", conn)

print(df.head())