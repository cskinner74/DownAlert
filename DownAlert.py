#!/usr/bin/python3

# Python script to report status of a URL
# Sends SMS alert if the request returns anything other than 200
# Or is unreachable

# Note: must create account with Twilio to get the account_sid and auth_token

import requests
import sys
import argparse
from twilio.rest import Client

#SMS setup
account_sid="*"
auth_token="*"
toNum="*"
fromnum="*"
client = Client(account_sid, auth_token)

#Parser section
parser = argparse.ArgumentParser(description="Checks uptime for specified URL")
parser.add_argument("url", help="URL to check")
parser.add_argument("-v", "--verbose", help="Verbose", action="store_true")
args = parser.parse_args()

#Check URL
if(args.verbose):
    print("Checking URL")
try:
    r = requests.head(args.url)
    if(args.verbose):
        print("Status Code:",r.status_code)
    code = str(r.status_code)
    if r.status_code == 200: #Connection Okay
        if(args.verbose):
            print("Condition okay!")
    else:
        if(args.verbose):
            print("Condition bad!")
        statusMsg = " status code returning "
        message = client.messages.create(
                to=toNum,
                from_=fromNum,
                body=args.url+statusMsg+code)
except requests.ConnectionError:
    if(args.verbose):
        print("Failed to connect, check URL for errors")
    message = client.messages.create(
            to=toNum,
            from_=fromNum,
            body="URGENT ALERT! Cannot connect to "+args.url+"!")

