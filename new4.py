# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:20:00 2021

@author: Sreemant
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "6FyIZ1mh_tTiIrS-X-mfP9R8N-C7R61Q0N1cjNPjZKKG"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print(mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["year","Month","Present Passengers Traffic"]], 
                                   "values": [[1949,10,112]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/be8e841b-9321-4802-a069-a9681012bfdd/predictions?version=2021-06-08', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predicitions = response_scoring.json()
print(predicitions)
