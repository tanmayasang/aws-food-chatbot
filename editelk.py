import pandas as pd 
import json 
df1 = pd.read_csv('restaurantselastic_csv.csv')
id = 0 
df1.columns = ['id', 'Cuisine', 'BusinessId']
print(df1.columns)

#df1.to_json('elkfile.json', orient = 'records',index = 'true')
with open("elkfile.json", "w") as outfile:
    for _,row in df1.iterrows():
        dict1 = {"index": {"_index": "restaurants", "_id": row['BusinessId']}}
        json.dump(dict1, outfile)
        id += 1
        outfile.write('\n')
        dict2 = {"cuisine": row['Cuisine'], "business_id": row['BusinessId']}
        json.dump(dict2, outfile)
        outfile.write('\n')



