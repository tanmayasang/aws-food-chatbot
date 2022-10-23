import pandas as pd
import json
import time

client_id = '52yWt2D7942eXXw-S7kpfA'
api_key = '2rM-mTtbYJuIcWd0Lib-vs1-ejbLdKJd3XxXfsSlrYKL8KIOt38YVBbjj1BUhrrTNmLIi3Lq95WrobyqjMb_x2kARYyFB3dq99gQfb-trX2kYK3MD4FIXTUYTmRQY3Yx'
from yelpapi import YelpAPI
yelp_api = YelpAPI(api_key)
cuisines = {
    'italian': [],
    'mexican': [],
    'chinese': [], 
    'indian': [],
    'thai':[ ]
    }
location = ['Manhattan, NY']

offsets = [x for x in range(0, 951,50)]

for cuisine in cuisines.keys():
  for offset in offsets:
    cuisines[cuisine].append(yelp_api.search_query(term = cuisine,location = location, limit = 50, offset = offset))
    
  




#print(cuisines)
cols = ['Cuisine','BusinessId', 'Name', 'Address','Coordinates', 'URL', 'NumberOfReviews', 'Rating', 'ZipCode']
#print(cols)
df = pd.DataFrame(columns = cols)
 
df.head()

for cuisine in cuisines.keys():
  yelp_responses = cuisines[cuisine]
  for yelp_response in yelp_responses:
    businesses = yelp_response['businesses']
    for business in businesses:
      #Add 2 new fields: Cuisine and r_id
      entry = {
          'Cuisine': cuisine,
          'BusinessId': business['id'],
          'Name': business['name'],
          'Address': business['location']['display_address'],
          'Coordinates': business['coordinates'],
          'URL': business['url'],
          'NumberOfReviews': business['review_count'],
          'Rating': business['rating'],
          'ZipCode': business['location']['zip_code']
      }
      df = df.append(entry, ignore_index=True)

df.to_csv('restaurants_dynamo_data.csv')
df2 = df[['Cuisine','BusinessId']]
df2.to_json('restaurants_elastic.json')
df2.to_csv('restaurantselastic_csv.csv')




#print(df.head())