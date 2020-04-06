
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


positive_wrd = set()
negative_wrd = set()
dentist_dict_review = []

with open('positive_words.txt', 'r') as file:
    for line in file:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        positive_wrd.add(currentPlace)
        
    
with open('negative_words.txt', 'r') as file:
    for line in file:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        negative_wrd.add(currentPlace)
        
with open('yelp_dentists.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            str_business_ID=row[0]
            gql_query = r'''
            {
                 reviews(business: "%s") {
                     total
                     review {
                         text
                     }
                 } 
             }
              '''%(row[0])
            try:
               
                response = requests.post(YGQL_URL, data=gql_query, headers=headers)
             
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                print('POST Success!')

            #deserializing the JASON payload
            json_data_dict = response.json()
            #reviews_dict= [b['text'] for b in json_data_dict['data']['reviews']['review']]
            reviews_dict= [v['text'].split() for v in json_data_dict['data']['reviews']['review']]
            words= set()
            for lists in reviews_dict:
                for word in lists:
                    words.add(word)
            my_list = list(words)
            dentist_dict_review.append({"id":row[0],"name":row[1],"text":my_list})
#            print(dentist_dict_review)
            dentist_wrd_count_list=[]
        
        for row in dentist_dict_review:
            postive_words_test = []
            review_words=row["text"]
            #print(dentist)
            positive_word_count = 0
            negative_word_count = 0
#           a= set(positive_wrd).intersection(words)
            for P_wrd in positive_wrd:
                if P_wrd in review_words:
                    postive_words_test.append(P_wrd)
                    positive_word_count=positive_word_count +1
                else:
                    positive_word_count
            
            
            for N_wrd in negative_wrd:
                if N_wrd in review_words:
                    negative_word_count=negative_word_count+1
                else:
                    negative_word_count
                   
     
            
            dentist_wrd_count_list.append({"id":row["id"],"name":row["name"],"p_w":positive_word_count,"n_w":negative_word_count})
            
#            print(dentist_wrd_count_list)
        max_positive=0
        max_negative=0
        for row in dentist_wrd_count_list:
            if row["p_w"] > max_positive:
                max_positive = row["p_w"]
                max_p_name = row["name"]
                max_p_id = row["id"]
            
                
            if row["n_w"] > max_negative:
                max_negative = row["n_w"]
                max_n_name = row["name"]
                max_n_id = row["id"]
        print(f"The reviews for Business id : {max_p_id} , Business Name: {max_p_name} contained the most positive words = {max_positive}\n")
#         
        print(f"The reviews for Business id : {max_n_id} , Business Name: {max_n_name } contained the most negative words = {max_negative}")
##               
#print(dentist_dict_review)
#print(positive_wrd)
#print(negative_wrd)
    
