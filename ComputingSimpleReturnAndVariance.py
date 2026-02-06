import json 
with open("weekly_stock_data_50.json", "r") as f:
    data=json.load(f)
# print(len(data["NFLX"].keys()))
count=len(data["NFLX"].keys())
Returns={}
for stock in data.keys():
    Return_values={}
    ptr=count
    for i in range(count-1):
        ST=data[stock][str(i)]["4. close"]
        # print(ST)
        # break
        ST_1=data[stock][str(i+1)]["4. close"]
        Return_values[ptr]=(float(ST)-float(ST_1))/float(ST_1)
        ptr=ptr-1
    Returns[stock]=Return_values

Expected_return={}

for stock in Returns.keys():

    sum=0
    for key in Returns[stock].keys():
        
        sum=sum+Returns[stock][key]
    K=sum/len(Returns[stock].keys())
    Expected_return[stock]=K






