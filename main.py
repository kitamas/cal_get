# FLASK = = = = = = = = = = = 
import flask
import json
import os
from flask import send_from_directory, request
# FLASK = = = = = = = = = = = 

# CRED = = = = = = = = = = =
import googleapiclient.discovery
from google.oauth2 import service_account as google_oauth2_service_account
# CRED = = = = = = = = = = =

# QUICKSTART = = = = = = = = = = =
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# QUICKSTART = = = = = = = = = = =


# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/authentication')

def authentication():
    creds = google_oauth2_service_account.Credentials.from_service_account_info(
    {
  "type": "service_account",
  "project_id": "my-project-90818-learn-hun",
  "private_key_id": "fb2290767b931edec50717a4812f772edfee176a",
  "private_key": "-----BEGIN PRIVATE KEY-----MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDZCkiBW2BjsphVBGmQWNBEH0K3679EdL5LxGW0ouugnfoF0+AQW8S5WD+DQmSqGmXai77p8FvuUkEfuDE153w/VDo4Py8xxrFEbtbiGiMS8MW5wB/fwezhzc47ox4GABOXKKshi+p5ohgg9F/fwtgy8g7l7DWmLpqNutV5OLj2BpGZ2Mn5EIXw5bwgZNxd0tH+OvZOSGWO/mAFTtscAqYedL2Azq+UA1GICFYRr10P5sbzIKttIuRhhh6pnHBrvCUxSgVxUxJJ70BFHxkIB6hBMi0t9eTC+7VFHwQbed7I7sTQpIHl0NYiBPpIVcdmFqNfwYHgJW+ACnBjc2htdfqVAgMBAAECggEAHc6gO4e5mqeV7SMgfk78N0bVyl2JlJS158DuuNqhIptfkXpSLNz1jQDWJCgzm/rpHxUPIKC+d2H7iKgqtfz3Htlp73yZ9iuT/9J7F21AgOLpPMPqfLfs2OwDVURnJKrRBfLzYbWN+6trxebZ3eir+X8t1ZzVl1+SIUHV/IJyQHNQqc5QwtZ91GW55ZFcoykhg3EfMnqSNQuv5kQ07YKMEQrr3IFTRIRGeblmZX7/41jwj3eJSda8QPsh7f9bzTbsokVXTcnrjLU6WondFU0PZC529j8BVlITshv+jnSyX3KUil1nfAyffo0OFCLR6Qd/aXty8X+QSyplLPILUBMudwKBgQD4PRJyxJ8+e9qs8ILqoxxumfc1kCnbew5ReXaERvFvQtA0nQ1cGCGi8U32kqSrZP/3ramTmTS2fSOjiipNKplT9MGiFVw9Y4/hR/gJnMEdzxxcbQTHAp5WR4R7OJrH2LQcXd5tAOZmq/GjRu/ja9VGViwkyagV31sXqJIcqIYufwKBgQDf037yeFe37GbvhZLWvIZxXoeSKiM9ynHCAgIH6VG8GJT3CWiBaM81ZMzUOo3nfF+8s2iJi8UpejJNIIS7GDbqoWCuBJ++gv/fVGi7OTZHvYFsyQVD/3BxCEdOYXL/U6NmMTbrMsLFRLYoSFoDqs2Ebm57/hXhgcbCdOeEgmi06wKBgHNKuhS/qU4169xCYCtl0kC0FZK1ABvFzWKdzSOmZ1/LYjPtdVT+iDDLbfBFL2HDKPb5mzbIAyl2eWTtOLRaQpgxpvUGgq6oXRy+dj7QpQiZNozevUdIug1MbgVkxs5moVBDcJijwF6TIUk6GxQ+8vEV+K6lUgHGmOImEqZoxtk1AoGALskjuQVEuLJWleyi0/YWWC49QmVCdpERlE8dI5A2wI2W3ch+qsZAwdVvJ1GSBfgufuA1ksK/lLrxNsP8WqtmF0diUR2wUn9JguI+/huoZ/iJzDZ8vkjvtQDY/t5JzmsqNZtF8oXqxpdlSChPgIK8cNkwiQSEiF27MTyEhGNKBb8CgYB1Tn05s5jJrnllz2C04uv3xI++wYgefyFE6KwBiEzwmXKWg0KyiW9uCIOufonAggjdZx8k1CEWWdzfwmLGcOyvqmooc4qAWz7zZDqVJOm5wN0qjympyVjshI7SLGshk9oUap5zS3O6QC4m+fS/03Q+XwpgARxw5DLUduI6nMzvwA==-----END PRIVATE KEY-----",
  "client_email": "appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com",
  "client_id": "115405775326578876255",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/appointment-scheduler%40my-project-90818-learn-hun.iam.gserviceaccount.com"
    },
    scopes=['https://www.googleapis.com/auth/calendar'],
    subject='appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com'
    )
    return creds

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)
    #text = "webhook flask text response"
    text = main()

    res = {
        "fulfillment_response": {"messages": [{"text": {"text": [text]}}]}
    }
    return res

def main():
    try:
        service = build('calendar', 'v3', credentials=authentication())

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        start_event = "" 
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            #print(start, event['summary'])
            #start_event += start_event + " | " + event['summary'] + " | " + start
            start_event += event['summary'] + " "  + start + " | "
            #return event['summary']

        return start_event

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == "__main__":

    app.run()