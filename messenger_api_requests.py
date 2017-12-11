# Script to send messages to FB Messenger via FB Messenger Send API
import requests

# Constants
FB_ACCESS_TOKEN = 'EAAFm0tQZAaVQBAFsNEISx9MYGZAUBDgHMzEeVxUt68rJiuZAUdDjtvsppmioP1ewR4XtBmulePRFQVQq3yrrqQl97IgNrSrAdZAzZAkDfLjsxa5O4eNVZCJ8G1zciJalWO8fKohgGn6iFBiZBCaprCyEGvWZBKJrIp4G0Co6ZAK9BZAgZDZD'
SEND_API_URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + FB_ACCESS_TOKEN

def send_message(messenger_id, text):
    # Package params into dictionaries for POST request
    recipient = {'id':messenger_id}
    message = {'text':text}
    params = {
        'recipient':recipient,
        'message':message
    }

    # Send POST request to Facebook Messenger Send API to send text message
    r = requests.post(SEND_API_URL, json=params)

def send_numbers_message(messenger_id,text,nums):
    quick_replies = []
    for i in nums:
        quick_replies.append({"content_type":"text", "title":i,"payload":i})

    recipient = {'id':messenger_id}
    message = {
        'text':text,
        'quick_replies':quick_replies
    }
    params = {
        'recipient':recipient,
        'message':message
    }

    # Send POST request to Facebook Messenger Send API to send message
    r = requests.post(SEND_API_URL, json=params)