import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

AUTH_HEADER = os.getenv("AUTH_HEADER")
BASE_URL = os.getenv("BASE_URL")

headers = {
    "Content-Type" : "application/json",
    "Authorization": AUTH_HEADER
}

def query_mail_policies(policy,headers,mode):
    ENDPOINT = f"api/v2.0/config/incoming_mail_policies/{policy}/senders_and_recipients?mode={mode}&device_type=esa"
    MAIL_POLICY_URI = BASE_URL + ENDPOINT
    response = requests.request("GET", MAIL_POLICY_URI, headers=headers)
    response_contentpart = json.loads(response.content)
    return (response_contentpart)

def main(policy,mode):
    mail_policy = query_mail_policies(policy,headers,mode)
    print (mail_policy)


if __name__ == "__main__":
    main(policy=input("Please specify the incoming mail policy you would like to fetch: "),mode=input("Please specify the machine mode- cluster or machine:"))
