
from __future__ import print_function # DEBUG
import sys # DEBUG
from flask import Flask, request, jsonify, g, Response,render_template
from peewee import *
import bot
import db
import os

# Setup
application = Flask(__name__)
database = db.database

# Opens a connection to our database when we receive a request and closes it after the request
@application.before_request
def before_request():
    try:
        database.connect()
    except:
        pass

@application.after_request
def after_request(response):
    try:
        database.close()
    except:
        pass
    return response

# Our typical routes
@application.route('/')
def hello_world():
    return 'Hello World! Nothing is broken!'

@application.route('/webhook', methods=['GET', 'POST'])
def webhook():
    try:
        if request.method == 'GET':
            # Webhook is verified with Facebook Messenger https://developers.facebook.com/docs/graph-api/webhooks
            if request.args.get('hub.verify_token') == '12345':
                return Response(request.args.get('hub.challenge'))
            else:
                return Response('Wrong validation token.')
        else:
            # Here messages in a form of JSON are received, code for this is handled in bot.py
            return bot.response_handler(request.get_json())
    except Exception as e:
        print(str(e), file=sys.stderr)
        return Response('Application error.')

if __name__ == '__main__':
    application.debug = True
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0',port = port, debug = True)