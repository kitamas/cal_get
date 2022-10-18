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
  "private_key_id": "cf8bd4105633c3cac528d1c8c4c66cc3b825e837",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeQrDkS5Rq/khX\nNoU01bLEbZHj/JjzwlcozMB0uRP+H9NYJytYrl4+vqhi3+EApY+bKpU/iB/A9tPC\nVIYjhXeACCXtNq6sz8hQDN6y+cKW5K4i2yd1xpeIlAXjo4M/uRIarlffgEi3MOAX\nRtTDskXvECuu2rXsIbgQEBzpCwJQhaVWnOHk4ONTJnEKSjvtuHXRZUc6GrabLrLU\nb4h1nDYh8+IVoUxpcZg0sW9XWpXw2O3kh8o6ADy4aH2KB9Sv4yktLLNcVWrqisei\nekA93NnWji5pG2DKuqjrmaZGA9SwOA5gT34EfrbL8zVFaEGgV7yp5ytrTg5vmtaw\nP36j58iJAgMBAAECggEAG5iV900NjYWXECwX2LFtuW5AuwBEHHc2Ew12/rN6Hr0m\ncW/tEUrgcLD2tD0FI0N7UcuAWGJwZQm1PaTW+hEvGAJzuJQpK8WUkI7Z81v1WDH6\ngmX0EMenC0ACceIEhCNNmpztgjHAnD73yF9HwPMQWkIX1+bXw5vSmGxy2hkbF3ac\nKehAlVB584QC8L191WtWPpx27pdNy2ncnlW6Xaail8NtGlCELLGrmicQUjgxZhsU\ngEZh/ZrTYm4ion5mWCYtbSvuXN++9Zy6kIdpYiFOroQuEr48L6l0KLmVvNsuZ1D0\nk4xdXJxtx0kacGr0tyg1VV3vut14vcSlDqbeDUy7DQKBgQC/5LuQVTJT3FiJ13sb\nCyJIuFVQAX2p1+TXsiKJh9Copaua0tvXygJtbGFEVmYKS3VwiC8OyESQQhATFORE\nYZYpek0UwhNggekg+asiMMSnPc/hHkxQdsxmT34sfmuooSeDvqrVPw6BW3i7Hb6Q\nB7lfydH+v6VejPKWm2q7sm6UpQKBgQDTIZJ/rdgknqnIENgcHwRJoKS3j2RcCvnK\nu0pXoumA9xq1/JFOCuGmRnscyga0d17fYGpER3iR5NL2YAksMSUEDyj+yFupHyfS\nTZzVVaeYNW3OKjDXwUDGYh2D3JkF7P6zeC9LLBkvwuhllvwC1URewWARBpreVGpH\nuZGRo6CLFQKBgHnO9yTif+TtzSIKr3F2OtgQcs8rcxpaGkC1KelFVjWHnIvV54lu\nCOZu0rtvYKyOQ8kgGUb351XvKYcDTvb9PzWrFbzkiSpMrLCq62/zpxFGUmvjMKwv\nDQaw1TXnNe3ABnZBlO1yboG8j8GvWuTQkmJ0mSFtg8qmC+OAWls1I66lAoGAZCvL\njBR5Nnao6ylCv6Tfrecv/39jCGCUv2E5FndO/kc/PxUEA9kZ0oAiLTiVEc6JDsZ5\n5MdcJyxAA3DxKSxv+YsP0kJRat5DUH5OaNFo4MiIvoY6AkPIbddjVYq2d59IAPKG\nzc2wbX62MG0ASH/THnn1EF7n35CBlGIw9L6DjzkCgYEAu0LhdTHuuM6DOAfh4ohw\n0oj2770Dyw0vQImp+4qbdocLqXIVOZYEIywGfi+OLuSxrSYsw2BuTAPAtIEmkuHx\n4cvV/XxcWWPY30B4Z2irOBIsIXJjfAO/DyCyDaX7Cmoy+NgoCwRSRzDeOiQ7ysw8\nhwrS/OoTx3BhHYJt+NO6qIM=\n-----END PRIVATE KEY-----\n",
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
    #print(req)

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
        # now = 2022-10-09T05:53:52.400939Z

        page_token = None

        # https://developers.google.com/calendar/api/v3/reference/calendarList/list
        # If you want to list the calendars that have been shared with a service account, you should first insert the corresponding calendars individually via CalendarList: insert.
        # https://developers.google.com/calendar/api/v3/reference/calendarList/insert
        # calendar_list_entry = {'id': 'r0evkror5p88vkhf3q842jk8fg@group.calendar.google.com'}
        # created_calendar_list_entry = service.calendarList().insert(body=calendar_list_entry).execute()
        # calendar_ids = ['61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com','r0evkror5p88vkhf3q842jk8fg@group.calendar.google.com']

        calendar_ids = []

        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                if '@group.calendar.google.com' in calendar_list_entry['id']:
                    calendar_ids.append(calendar_list_entry['id'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break

        # start_date = datetime.datetime(2022, 10, 14, 0, 0, 0, 0).isoformat() + 'Z'
        end_date = datetime.datetime(2022, 10, 30, 23, 59, 59, 0).isoformat() + 'Z'

        for calendar_id in calendar_ids:
            events_result = service.events().list(
                calendarId=calendar_id,
                #timeMin=start_date,
                timeMin=now,
                timeMax=end_date,
                singleEvents=True,
                orderBy='startTime').execute()
            events = events_result.get('items', [])
            # tags from the calendar, for filtering
            # if "description" exists in the calendar: event['description']
            # if "status":"confirmed",

            if calendar_id == '61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com':
                events_cal1 = "CAL1: " 
                for event in events:
                    time_cal1_ISO = event['start'].get('dateTime', event['start'].get('date'))
                    # 2022-10-15T10:00:00+02:00
                    time_cal1_obj = datetime.datetime.fromisoformat(time_cal1_ISO)

                    date = time_cal1_obj.strftime("%Y-%m-%d %B %A")
                    time = time_cal1_obj.strftime("%H:%M")

                    weekday = time_cal1_obj.weekday()

                    events_cal1 += event['summary'] + " | " + date + " " + time + " | "

            events_cal2 = "CAL2: " 
            for event in events:
                time_cal2_Z = event['start'].get('dateTime', event['start'].get('date'))
                # 2022-10-15T10:00:00Z
                #time_cal2 = datetime.datetime.strptime(time_cal2_Z,'%Y-%m-%dT%H:%M:%S%z')
                events_cal2 +=  event['summary'] + " | " + time_cal2_Z + " | "

        if not events:
            print('No upcoming events found.')
            return

        # NOW =  2022-10-17T06:20:26.706507Z END DATE =  2022-12-31T23:59:59Z
        # START TIME =  2022-10-17 08:20:27.944570 END TIME =  2022-12-31 23:59:59

        startTime = datetime.datetime.utcnow() + datetime.timedelta(hours = 2)
        endTime = datetime.datetime(2022, 12, 31, 23, 59, 59, 0)

        duration = datetime.timedelta(hours = 1)

        f_obj = findFirstOpenSlot(events,startTime,endTime,duration)
        print("fobj",type(f_obj))
        if f_obj = None:
            print("NONE NONE")
        else:
            f_time = f_obj.strftime("%Y-%m-%d %H:%M")
        firsto = "FIRST OPEN: "        
        print(firsto,f_time)

        return events_cal1 + events_cal2 + firsto + f_time

    except HttpError as error:
        print('An error occurred: %s' % error)


# https://stackoverflow.com/questions/72205649/find-an-open-slot-in-google-calendar-api-between-time
# https://www.pythonfixing.com/2022/05/fixed-find-open-slot-in-google-calendar.html

def findFirstOpenSlot(events,startTime,endTime,duration):

    def parseDate(rawDate):
        # RAWDATE =  2022-10-17T09:00:00Z
        #Transform the datetime given by the API to a python datetime object.
        #return datetime.datetime.strptime(rawDate[:-6]+ rawDate[-6:].replace(":",""), '%Y-%m-%dT%H:%M:%S%z')

        parse = datetime.datetime.strptime(rawDate,'%Y-%m-%dT%H:%M:%SZ')
        # PARSE =  2022-10-18 11:00:00 <class 'datetime.datetime'>

        return datetime.datetime.strptime(rawDate, '%Y-%m-%dT%H:%M:%SZ')

    eventStarts = [parseDate(e['start'].get('dateTime', e['start'].get('date'))) for e in events]

    eventEnds = [parseDate(e['end'].get('dateTime', e['end'].get('date'))) for e in events]

                #for event in events:
                    #time_cal1_ISO = event['start'].get('dateTime', event['start'].get('date'))

    #eventStarts = [e['start'].get('dateTime', e['start'].get('date')) for e in events]
    #['2022-10-17T09:00:00Z'] <class 'list'>
    #eventEnds = [e['end'].get('dateTime', e['end'].get('date')) for e in events]

    gaps = [start-end for (start,end) in zip(eventStarts[1:], eventEnds[:-1])]

    print("start = eventStarts = ",eventStarts,"end = eventEnds = ", eventEnds,"gaps = ",gaps)
    # start =  ['2022-10-17T19:00:00Z'] end = ['2022-10-17T20:00:00Z'] gaps =  []

    if startTime + duration < eventStarts[0]:
        # A slot is open at the start of the desired window.
        return startTime

    for i, gap in enumerate(gaps):
        if gap > duration:
            #This means that a gap is bigger than the desired slot duration, and we can "squeeze" a meeting.
            #Just after that meeting ends.
            return eventEnds[i]

    #If no suitable gaps are found, return none.
    return None

if __name__ == "__main__":

    app.run()