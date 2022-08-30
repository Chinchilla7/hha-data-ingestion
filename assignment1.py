#importing packages for this assignment
import pandas as pd ## import pandas for general file types 
import json ## import json for json files
import requests ## import requests for web requests
from google.cloud import bigquery ## import bigquery for bigquery files'
import xlrd ## import xlrd for excel files, tab names 

#Section 1 bring in .xls file with first tab as 'tab1' and second tab 'tab2'
#import xls file
df = pd.read_excel('data/Educational_suicide.xls')
df
#tab names in xls file
xls = xlrd.open_workbook('data/Educational_suicide.xls', on_demand=True)
xls.sheet_names()
#bringing in first tab 'tab1' as a dataframe
df1 = pd.read_excel('data/Educational_suicide.xls', sheet_name='tab1')
df1
#bringing in second tab 'tab2' as a dataframe
df2 = pd.read_excel('data/Educational_suicide.xls', sheet_name='tab2')
df2

#Section 2 bring in open source json API via requests and json package
#bringing in the json API from CMS 
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/60ccbf1c-d3f5-4354-86a3-465711d81c5a/data')
#preview data using json
apiDataset = apiDataset.json()
#showing results 
apiDataset 

#Section 3 Bringing in 2 open source bigquery datasets
#connecting to bigquery via a client
client = bigquery.Client.from_service_account_json('/Users/reginachen/Downloads/regina-507-9ef3317126d6.json')
#limiting queries to 100 rows each for first dataset
query_job = client.query("SELECT*FROM `bigquery-public-data.fda_food.food_events` LIMIT 100")
#getting results of query
results = query_job.result()
# Putting results in dataframe
bigquery1 = pd.DataFrame(results.to_dataframe())
#limiting queries to 100 rows each for second dataset
query_job = client.query("SELECT*FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
#getting results of query
results = query_job.result()
# Putting results in dataframe
bigquery2 = pd.DataFrame(results.to_dataframe())

