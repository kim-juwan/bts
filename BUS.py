import pandas as pd 
import os
import numpy as np 
import codecs

df = pd.read_excel('./bus.xlsx',header=3)
print(df.head())
print(df.isnull().sum())