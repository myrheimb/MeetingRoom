import datetime
from exchangelib import Credentials, Account, EWSDateTime, EWSTimeZone, CalendarItem
from exchangelib.folders import Calendar
import loginCredentials
import time

# This is run to check if it is currently daylight saving time or not, and saves it into the variable dst.
# If dst == 1 it's summer and if dst == 0 it's winter.
dst = time.localtime().tm_isdst

busyTimes = []
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

# Tries to list today's meetings (10 occurrences).
try:
    meetingStartTime01 = (str(calendarItems[0][0])[11:16])
    meetingEndTime01 = (str(calendarItems[0][1])[11:16])
    print ('Title:', calendarItems[0][2])
    print ('Start time:', meetingStartTime01)
    print ('End time:', meetingEndTime01)
    print ('Organizer:', calendarItems[0][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime01.replace(":","")),int(meetingEndTime01.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime02 = (str(calendarItems[1][0])[11:16])
    meetingEndTime02 = (str(calendarItems[1][1])[11:16])
    print ('Title:', calendarItems[1][2])
    print ('Start time:', meetingStartTime02)
    print ('End time:', meetingEndTime02)
    print ('Organizer:', calendarItems[1][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime02.replace(":","")),int(meetingEndTime02.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime03 = (str(calendarItems[2][0])[11:16])
    meetingEndTime03 = (str(calendarItems[2][1])[11:16])
    print ('Title:', calendarItems[2][2])
    print ('Start time:', meetingStartTime03)
    print ('End time:', meetingEndTime03)
    print ('Organizer:', calendarItems[2][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime03.replace(":","")),int(meetingEndTime03.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime04 = (str(calendarItems[3][0])[11:16])
    meetingEndTime04 = (str(calendarItems[3][1])[11:16])
    print ('Title:', calendarItems[3][2])
    print ('Start time:', meetingStartTime04)
    print ('End time:', meetingEndTime04)
    print ('Organizer:', calendarItems[3][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime04.replace(":","")),int(meetingEndTime04.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime05 = (str(calendarItems[4][0])[11:16])
    meetingEndTime05 = (str(calendarItems[4][1])[11:16])
    print ('Title:', calendarItems[4][2])
    print ('Start time:', meetingStartTime05)
    print ('End time:', meetingEndTime05)
    print ('Organizer:', calendarItems[4][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime05.replace(":","")),int(meetingEndTime05.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime06 = (str(calendarItems[5][0])[11:16])
    meetingEndTime06 = (str(calendarItems[5][1])[11:16])
    print ('Title:', calendarItems[5][2])
    print ('Start time:', meetingStartTime06)
    print ('End time:', meetingEndTime06)
    print ('Organizer:', calendarItems[5][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime06.replace(":","")),int(meetingEndTime06.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime07 = (str(calendarItems[6][0])[11:16])
    meetingEndTime07 = (str(calendarItems[6][1])[11:16])
    print ('Title:', calendarItems[6][2])
    print ('Start time:', meetingStartTime07)
    print ('End time:', meetingEndTime07)
    print ('Organizer:', calendarItems[6][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime07.replace(":","")),int(meetingEndTime07.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime08 = (str(calendarItems[7][0])[11:16])
    meetingEndTime08 = (str(calendarItems[7][1])[11:16])
    print ('Title:', calendarItems[7][2])
    print ('Start time:', meetingStartTime08)
    print ('End time:', meetingEndTime08)
    print ('Organizer:', calendarItems[7][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime08.replace(":","")),int(meetingEndTime08.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime09 = (str(calendarItems[8][0])[11:16])
    meetingEndTime09 = (str(calendarItems[8][1])[11:16])
    print ('Title:', calendarItems[8][2])
    print ('Start time:', meetingStartTime09)
    print ('End time:', meetingEndTime09)
    print ('Organizer:', calendarItems[8][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime09.replace(":","")),int(meetingEndTime09.replace(":",""))+1))]
except:
    pass

try:
    meetingStartTime10 = (str(calendarItems[9][0])[11:16])
    meetingEndTime10 = (str(calendarItems[9][1])[11:16])
    print ('Title:', calendarItems[9][2])
    print ('Start time:', meetingStartTime10)
    print ('End time:', meetingEndTime10)
    print ('Organizer:', calendarItems[9][3].name)
    busyTimes = busyTimes+[list(range(int(meetingStartTime10.replace(":","")),int(meetingEndTime10.replace(":",""))+1))]
except:
    pass

# Changes the list busyTimes from a list containing lists to a single list.
busyTimesFlat = [item for sublist in busyTimes for item in sublist]

# Function to book a meeting directly on the screen. Standard title is "Booked on screen".
# The meeting start and end time is defined by the user when run.
# To avoid double booking a check is run to see if the start and/or end time is in conflict with an already booked meeting.
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

bookMeeting()
