from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar.events'

def calAdd(posts):
    # Load credentials.json
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    for p in posts:
        event = {
          'summary': '[%s限] %s(%s, %s)' % (p['time'], p['course'], p['class'], p['teacher']),
          'description': p['misc'],
          'start': {
            'date': p['day'],
            'timeZone': 'Asia/Tokyo',
          },
          'end': {
            'date': p['day'],
            'timeZone': 'Asia/Tokyo',
          },
        }

        CAL_ID = 'm771ihgg5fehhb2103ek6md31g@group.calendar.google.com'
        result = service.events().insert(calendarId=CAL_ID, body=event).execute()
        print('Event created: %s' % (result.get('htmlLink')))


if __name__ == '__main__':
    calAdd(posts = [{
           'time': '2',
           'course': 'SampleLecture',
           'class': 'A',
           'teacher': 'John Doe',
           'misc': 'hello world',
           'day': '2018-11-30'
           }])

