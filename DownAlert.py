#!/usr/bin/python3

# Python script to report status of a URL
# Sends Slack alert if the request returns anything other than 200
# Or is unreachable

import requests
import sys
import argparse
import configparser
import json

#Argument parsing
parser = argparse.ArgumentParser(description="Checks uptime for specified URL")
parser.add_argument("url", help="URL to check")
parser.add_argument("-v", "--verbose", help="Verbose", action="store_true")
args = parser.parse_args()

#Config parsing
config = configparser.ConfigParser()
config.read('config.ini')
webhook = config.get('Main', 'webhook')

#Check URL format
if not args.url.startswith('http'):
    print("Please provide schema: http:// or https://")
    exit(1)

#Check URL status
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
    slack_data = 'URGENT ALERT! Cannot connect to: ' + args.url
    slack_response = requests.post(
            webhook, data=json.dumps({'text': slack_data}),
            headers={'Content-Type': 'application/json'})
    if slack_response.status_code is not 200:
        raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (slack_response.status_code, slack_response.text))

