Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

#change working directory
import os
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
os.chdir('Users/kathi/Desktop/dgthg')
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

#import data set
import pandas as pd

df = pd.read_excel (r'X:/Users/kathi/Desktop/dgthg/TAA_Kathi_DGTHG_anonymisiert.xlsx')
