import requests
import json
import pandas as pd


data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)

# print(pd.DataFrame(results))

df1 = pd.json_normalize(results)
print(df1)

cherry = df1.loc[df1["name"] == "Cherry"]
(cherry.iloc[0]["family"]), (cherry.iloc[0]["genus"])

print(cherry)

cal_banana = df1.loc[df1["name"] == "Banana"]
cal_banana.iloc[0]["nutritions.calories"]
print(cal_banana)


data2 = requests.get("http://dog-api.kinduff.com/api/facts")
results2 = json.loads(data2.text)

df2 = pd.DataFrame(results2)
df2.drop(columns="success", inplace=True)
print(df2)
