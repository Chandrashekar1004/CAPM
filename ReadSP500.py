import csv
import pandas as pd

data=pd.read_csv("SP500.csv",header=None, names=['Date', 'Close'])
# print(data.keys())
data=data.drop(index=0)
count=len(data)
ptr=count
Market_return={}
# print(data.iloc[count-1]["Close"])
for i in range(count-1):
        ST=data.iloc[count-i-1]["Close"]
        # print(ST)
        # break
        ST_1=data.iloc[count-i-2]["Close"]
        Market_return[ptr]=(float(ST)-float(ST_1))/float(ST_1)
        ptr=ptr-1
# print(Market_return)