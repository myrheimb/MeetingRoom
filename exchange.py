import datetime
from exchangelib import Credentials, Account, EWSDateTime, EWSTimeZone, CalendarItem
from exchangelib.folders import Calendar
import loginCredentials
import time

''' calendarIteration is a function that saves all of today's meetings into a dictionary, and all the busy times into a list called busyTimesFlat.

To check if it is currently daylight saving time or not, and saves it into the variable dst.
If dst == 1 it's summer and if dst == 0 it's winter.

It then gets the login credentials from the loginCredentials.py file and logs into Microsoft Exchange.
After it's logged in, it saves all of today's meetings into a list called calendarItems.
Lastly a for loop is run through the items in the calendarItems list and saves the meetings start and end times, title and organizer into the dictionary meetingDict.'''

def calendarIteration():
    dst = time.localtime().tm_isdst
    calendarItems = []
    now = datetime.datetime.now()
    day, month, year = now.day, now.month, now.year
    tz = EWSTimeZone.timezone('Europe/Oslo')
    credentials = Credentials(username=loginCredentials.login['username'], password=loginCredentials.login['password'])
    account = Account(loginCredentials.login['account'], credentials=credentials, autodiscover=True)
    items = account.calendar.view(
        start=tz.localize(EWSDateTime(year, month, day)),
        end=tz.localize(EWSDateTime(year, month, day)) + datetime.timedelta(days=1),
        )
    if dst == 0:
        for item in items:
            today_events = [item.start + datetime.timedelta(hours=1), item.end + datetime.timedelta(hours=1), item.subject, item.organizer]
            calendarItems.append(today_events)
    else:
        for item in items:
            today_events = [item.start, item.end, item.subject, item.organizer]
            calendarItems.append(today_events)
    startTimeName = 'meetingStartTime_'
    endTimeName = 'meetingEndTime_'
    titleName = 'meetingTitle_'
    organizerName = 'meetingOrganizer_'
    counter0 = 0
    counter1 = 1
    counter2 = 2
    global meetingDict
    global busyTimes
    global busyTimesFlat
    meetingDict = {}
    busyTimes = []
    for events in calendarItems:
        try:
            meetingDict[startTimeName+str(counter1)] = (str(calendarItems[counter0][0])[11:16])
            meetingDict[endTimeName+str(counter1)] = (str(calendarItems[counter0][1])[11:16])
            meetingDict[titleName+str(counter1)] = (calendarItems[counter0][2])
            meetingDict[organizerName+str(counter1)] = (calendarItems[counter0][3].name)
            busyTimes = busyTimes+[list(range(int(meetingDict['meetingStartTime_'+str(counter1)].replace(':','')),int(meetingDict['meetingEndTime_'+str(counter1)].replace(':',''))+1))]
            busyTimesFlat = [item for sublist in busyTimes for item in sublist]
            counter0 = counter1
            counter1 = counter2
            counter2 += 1
        except:
                pass

'''  bookMeeting is a function to book a meeting directly on the screen. Standard title is 'Booked on screen'.
The meeting start and end time is defined by the user when run.
To avoid double booking a check is run to see if the start and/or end time is in conflict with an already booked meeting. '''

def bookMeeting():
    startTime = input('Write start time: ')
    endTime = input('Write end time: ')
    if int(startTime)+1 in busyTimesFlat or int(endTime)-1 in busyTimesFlat:
        print('There is already a meeting in the selected time period. Try again with a new start and/or end time.')
        bookMeeting()
    else:
        item = CalendarItem(folder=account.calendar, subject='Booked on screen', start=tz.localize(EWSDateTime(year, month, day, int(startTime[0:2]), int(startTime[2:4]))), end=tz.localize(EWSDateTime(year, month, day, int(endTime[0:2]), int(endTime[2:4]))))
        item.save()
        print('Meeting booked OK.')

calendarIteration()
bookMeeting()
