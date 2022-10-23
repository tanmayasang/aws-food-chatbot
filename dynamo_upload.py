import json
import os
import boto3
import csv
import pandas as pd
import datetime
from decimal import Decimal
from datetime import datetime

def lambda_handler(event, context):

 s3_client = boto3.client('s3') 
 csvfile = s3_client.get_object(Bucket='restaurant-csv-1', Key= 'restaurants_dynamo_data.csv') 
 r_df = pd.read_csv(csvfile.get("Body"))
 dclient = boto3.client('dynamodb')
 for _,row in r_df.iterrows():
  dclient.put_item(TableName='yelp-restaurants', Item={'insertedAtTimestamp': {'S': str(datetime.now())},'BusinessId':{'S':row['BusinessId']}, 'Name':{'S':row['Name']}, 'Cuisine':{'S':row['Cuisine']}, 'Address':{'S':row['Address']},  'Coordinates':{'S':row['Coordinates']}, 'NumberOfReviews':{'S':str(row['NumberOfReviews'])}, 'Rating': {'S':str(row['Rating'])},'ZipCode': {'S':str(row['ZipCode'])}})
 
                
 
