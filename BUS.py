import pandas as pd 
import os
import numpy as np 
import codecs

df = pd.read_csv('./bus.csv',encoding='euc-kr')
print(df.head())
print(df.isnull().sum())