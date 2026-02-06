import json 
with open("weekly_stock_data.json", "r") as f:
    data=json.load(f)

stock={}

for d in data.keys():
    stock_data={}
    count=0
    for i in data[d]["Weekly Time Series"].keys():
        stock_data[count]=data[d]["Weekly Time Series"][i]
        stock_data[count]["date"]=i
        count+=1
        if count==50:
            break
    stock[d]=stock_data

#########Hardcoded because of share split############
ptr=1
for i in stock["NFLX"].keys():
    ptr+=1
    if ptr<7:
        for key in stock["NFLX"][i].keys():
            # print(stock["NFLX"][i][key])
            if key!="date":
                stock["NFLX"][i][key]=float(stock["NFLX"][i][key])
    elif ptr>7:
        for key in stock["NFLX"][i].keys():
            # print(stock["NFLX"][i][key])
            if key!="date":
                stock["NFLX"][i][key]=float(stock["NFLX"][i][key])/10

with open("weekly_stock_data_50.json", "w") as f:
    json.dump(stock, f, indent=4)
