import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

#set auth headers
AUTH_HEADER = os.getenv("AUTH_HEADER")
BASE_URL = os.getenv("BASE_URL")

def add_sender_to_mail_policy(sender,policy,mode):
	#URI for API Endpoint
	ENDPOINT = f"api/v2.0/config/incoming_mail_policies/{policy}/senders_and_recipients?mode={mode}&device_type=esa"
	MAIL_POLICY_APPEND_URI = BASE_URL + ENDPOINT

	headers = {
		"Content-Type" : "application/json",
		"Authorization" : AUTH_HEADER
	}

	payload = json.dumps({'data' : {'sender_config': {'sender': {'domain_entries': [sender]}}, 'receiver_config': {'operation': 'or', 'receiver': {'domain_entries': ['ANY']}}}})

	response=requests.request("POST", MAIL_POLICY_APPEND_URI, headers=headers, data=payload)
	response_content_part = json.loads(response.content)
	print(json.dumps(response_content_part, indent=2))

def main(sender,policy,mode):
	add_sender_to_mail_policy(sender,policy,mode)

if __name__ == "__main__":
	main(sender=input("Sender to add to mail policy:"),policy=input("Specify mail policy to add sender to:"),mode=input("Specify if this device is in cluster or machine mode:"))
