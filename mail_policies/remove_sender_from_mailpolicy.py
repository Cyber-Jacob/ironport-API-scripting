import json
import os
import requests
from query_mail_policies import query_mail_policies
from dotenv import load_dotenv

load_dotenv

AUTH_HEADER = os.getenv("AUTH_HEADER")
BASE_URL = os.getenv("BASE_URL")

headers = {
	"Content-Type" : "application/json",
	"Authorization" : AUTH_HEADER
	}

#Cisco AsyncOS recommends using a PUT request to update mail policies using their API. So we will construct a PUT Request
def update_mail_policy_PUT_request(policy,mail_policy_object,mode):
	ENDPOINT = f"api/v2.0/config/incoming_mail_policies/{policy}/senders_and_recipients?mode={mode}&device_type=esa"
	MAIL_POLICY_UPDATE_URI= BASE_URL + ENDPOINT
	response = requests.request("PUT",MAIL_POLICY_UPDATE_URI,headers=headers,data=json.dumps(mail_policy_object))
	response_content = json.loads(response.content)
	print(response_content)
	return(response_content)

def remove_sender_from_mail_policy(policy,sender,mode):
	mail_policy_object = query_mail_policies(policy,headers,mode)
	entries = mail_policy_object.get("data",[])

	updated_entries = []

	sender_object = {'sender_config': {'sender': {'domain_entries': [sender]}}, 'receiver_config': {'operation': 'or', 'receiver': {'domain_entries': ['ANY']}}}
	print(f"Current mail policy entries are as follows: \n{entries}")

	if sender_object in entries:
		entries.remove(sender_object)
		updated_mail_policy_object = {"data" : entries}
		print(f"Updated mail policy entries as follows: \n{entries}")
		update_mail_policy_PUT_request(policy,updated_mail_policy_object,mode)
	else:
		print(f"Sender {sender} not found in the specified mail policy.")

def main(policy,sender,mode):
	remove_sender_from_mail_policy(policy,sender,mode)

if __name__ == "__main__":
	main(policy=input("Please specify the mail policy to remove sender from: "),sender=input("Please enter sender to remove from specified mail policy: "),mode=input("please enter device mode-- machine or cluster: "))
