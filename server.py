import eel, time, exchange, os
from apscheduler.schedulers.background import BackgroundScheduler

# Initiates the web folder in the hierarchy.
eel.init('web')

# A function that triggers a JavaScript function that navigates to today in the calendar view.
def nextDayPython():
    eel.nextDay()

# Get updated calendar information from Exchange every 5 seconds.
def getExchangeEventsThread():
    while True:
        exchange.calendarIteration()
        eel.sleep(5.0)

# Check for room availability by comparing the current time to the list of busy times (busyTimesFlat).
# This is run after waiting 5 seconds for the calendar information to be updated and then every 5 seconds after.
def roomAvailabilityThread():
    while True:
        eel.sleep(5.0)
        exchange.roomAvailability()

# Set up a scheduled event that runs nextDayPython daily at 5am.
def nextDayThread():
    scheduler = BackgroundScheduler()
    scheduler.add_job(nextDayPython, 'cron', hour=5, minute=0)
    scheduler.start()

# Starts the function to get updated calendar information in its own thread.
eel.spawn(getExchangeEventsThread)

# Starts the function to check room availability in its own thread.
eel.spawn(roomAvailabilityThread)

# Starts the function to navigate to today in the calendar view in its own thread.
eel.spawn(nextDayThread)

# Settings to run Chrome in kiosk mode if eel.start is run with the web_app_options.
web_app_options = {
    'mode': 'chrome-app',
    'chromeFlags': ['--kiosk']
}

# Because of Raspberry Pi's modest hardware, a 2 second delay is added
# to make sure the needed information is collected from Exchange before running.
eel.sleep(2)

# eel.start('main.html', size=(800, 480)) # Uncomment this for the application to run in a broswer window.
# eel.start('main.html', options=web_app_options) # Uncomment this for the application to run in Chrome's kiosk mode.
