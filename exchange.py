import eel
import datetime
from exchangelib import Credentials, Account, EWSDateTime, EWSTimeZone, CalendarItem
from exchangelib.folders import Calendar, Message, Mailbox
from config import config
import time
import json

''' calendarIteration is a function that saves all of today's meetings/events into a list of dictionaries called meetingList,
and all the busy times into a list called busyTimesFlat.

First it checks to see if it is currently daylight saving time or not, and saves it into the variable dst.
If dst == 1 it's summer and if dst == 0 it's winter.

It then gets the login credentials from the loginCredentials.py file and logs into Microsoft Exchange.
After it's logged in it saves all of today's meetings/events into a list called calendarItems.

Lastly a for loop is run through the items in the calendarItems list which saves each meeting's
start times, end times and organizer into the dictionary meetingList and is then dumped into a events.json file located in the web folder. '''

def calendarIteration():
    global meetingList, busyTimes, busyTimesFlat, account, tz, year, month, day
    dst = time.localtime().tm_isdst
    calendarItems = []
    now = datetime.datetime.now()
    day, month, year = now.day, now.month, now.year
    tz = EWSTimeZone.timezone('Europe/Oslo')
    credentials = Credentials(username=config['username'], password=config['password'])
    account = Account(config['account'], credentials=credentials, autodiscover=True)
    items = account.calendar.view(
        start=tz.localize(EWSDateTime(year, month, day)),
        end=tz.localize(EWSDateTime(year, month, day)) + datetime.timedelta(days=1),
        )
    if dst == 0:
        for item in items:
            today_events = [item.start + datetime.timedelta(hours=1), item.end + datetime.timedelta(hours=1), item.organizer]
            calendarItems.append(today_events)
    else:
        for item in items:
            today_events = [item.start, item.end, item.organizer]
            calendarItems.append(today_events)
    meetingList = []
    busyTimes = []
    busyTimesFlat = []
    counter = 0
    for events in calendarItems:
        tempDict = {'start':str(calendarItems[counter][0]), 'end':str(calendarItems[counter][1]), 'title':calendarItems[counter][2].name}
        busyTimes = busyTimes+[list(range(int(tempDict['start'][11:16].replace(':','')),(int(tempDict['end'][11:16].replace(':','')))+1))]
        busyTimesFlat = [item for sublist in busyTimes for item in sublist]
        meetingList.append(tempDict)
        counter += 1
    with open('web/events.json', 'w') as f:
        f.write(json.dumps(meetingList))
        f.close()

'''  bookMeeting is a function to book a meeting directly on the screen. Standard title is 'Booked on meeting room screen'.
The meeting's start and end time is defined by the user in the application using a time picker on the newmeeting.html page.
To avoid double booking an if statement checks to see if any time between the start and end time is in conflict with an already booked meeting.
If there is a conflict, an alert in the application is shown to inform the user by running the JavaScript function alertBusy in newmeeting.html.
If there is no conflict, the meeting is saved and calendarIteration is run to immediately update the calendar in the application.
Lastly the application is redirected to the main page by using a JavaScript function called redirectMain. '''

@eel.expose
def bookMeeting(arg1, arg2):
    calendarIteration()
    startTime = str(arg1)
    endTime = str(arg2)
    if (any(x in range(int(startTime)+1,int(endTime)) for x in busyTimesFlat)):
        eel.alertBusy()
    else:
        item = CalendarItem(folder=account.calendar, subject='Booked on meeting room screen', start=tz.localize(EWSDateTime(year, month, day, int(startTime[:2]), int(startTime[-2:]))), end=tz.localize(EWSDateTime(year, month, day, int(endTime[0:2]), int(endTime[2:4]))))
        item.save()
        calendarIteration()
        eel.redirectMain()

''' The roomAvailability function checks if the current time is in the list of busy times or not
and triggers a JavaScript function called busyBackground if it is, and availableBackground is it's not. '''

@eel.expose
def roomAvailability():
    now = str(datetime.datetime.now())
    nowTime = now[11:13]+now[14:16]
    if int(nowTime)+1 in busyTimesFlat or int(nowTime)-1 in busyTimesFlat:
        eel.busyBackground()
    else:
        eel.availableBackground()

''' The sendMail function is made to enable the user to easily inform the IT department of any problems with the meeting room's AV equipment.
Any mail sent is also saved in the meeting room's sent mail folder. '''

@eel.expose
def sendMail(arg1, arg2):
    a = Account(config['account'], credentials=Credentials(username=config['username'], password=config['password']), autodiscover=True)
    m = Message(
    	account = a,
    	folder = a.sent,
    	subject = arg1,
    	body = arg2,
    	to_recipients = [Mailbox(email_address=config['mail'])],
    )
    try:
        m.send_and_save()
        print("Mail about " + arg1 + "is sent.")
    except:
        print("Mail about " + arg1 + " failed.")

''' The following 3 functions makes the name of the meeting room and the help desk's phone number and mail address available to use by JavaScript/HTML. '''

@eel.expose
def getRoomNamePy():
    return config['name']

@eel.expose
def getPhoneNumberPy():
    return config['phone']

@eel.expose
def getMailAddressPy():
    return config['mail']
