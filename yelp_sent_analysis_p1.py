
import requests
import json
import csv
from operator import itemgetter
from requests.exceptions import HTTPError
from pprint import pprint as pp

# Declare some str vars to hold immutable URLs

YGQL_URL = 'https://api.yelp.com/v3/graphql'

'''
STEP 1: Request a Client ID and Client Secret from FatSecret
'''

API_KEY = 'fDI-ka8iQSOUpQMRjxKI_pTqi_gulLL-b1EnIZXaqso-wlPVpXz8V4AH9LiSmVT5fisYbaDKsjT0njVWgxU2nemQmAAFTYPo5Ceu5IcW5Ln3jJxG0fSdZDG0ZHx_XXYx'

'''
Step 2. Using the API key to call an YGQL Endpoint
'''
headers = {
    # combine the strings  'Bearer' and API key
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/graphql',
    'Accept-Language': 'en_US',
}

# Declare a multi-line string for the query.  Easier to read...
gql_query = r'''
{
  search(term: "Dentists",
         location: "Downtown, pittsburgh, pa"
         limit:50
         sort_by:"best_match") {    
    business {
      id
      name
      rating      
    }
  }
}
'''

try:
    # Notice the request is a HTTP POST. That's because this requests
    # causes a change on the server.  Specifically, Yelp tracks usage of 
    # their GQL interface. You are "cut-off" if you abuse the the API - usage wise.
    #
    response = requests.post(YGQL_URL, data=gql_query, headers=headers)
    # If the response was successful, no Exception will be raised
    # by the following line
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('POST Success!')

# deserialize the JSON payload
json_data_dict = response.json()

#
#biz_ratings_dict = {}
#biz_dict = {}

biz_ratings_dict = []
biz_dict = {}

for b in json_data_dict['data']['search']['business']:
    biz_id = b['id']
    biz_name = b['name']
    biz_rating = b['rating']
    biz_ratings_dict.append({'id':str(biz_id ),'name':str(biz_name),'rating':str(biz_rating)})
biz_ratings_dict=sorted(biz_ratings_dict, key=itemgetter('rating'),reverse = True)
print(biz_ratings_dict)

     
with open('yelp_dentists.csv', mode='w', newline='') as csv_file:
     writer=csv.writer(csv_file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
     writer.writerow(['Business_id','Dentist Names', 'Ratings'])

     for row in biz_ratings_dict:
         writer.writerow([row['id'],row['name'],row['rating']])




