import csv
import pandas as pd
import numpy as np
data=pd.read_csv("Risk_Free.csv",header=None, names=['Date', 'Close'])
# print(data.keys())
data=data.drop(index=0)
count=len(data)
ptr=count
RF_return={}
# print(data.iloc[count-1]["Close"])
for i in range(count-1):
        ST=data.iloc[count-1-i]["Close"]
        # print(ST)
        # break
        ST_1=data.iloc[count-2-i]["Close"]
        RF_return[ptr]=(float(ST)-float(ST_1))/float(ST_1)
        ptr=ptr-1
Risk_free_return=np.mean(np.array(list(RF_return.values())))
