import eel
import time
import exchange

# Initiates the web folder in the hierarchy.
eel.init('web')

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

# Starts the function to get updated calendar information in its own thread.
eel.spawn(getExchangeEventsThread)

# Starts the function to check room availability in its own thread.
eel.spawn(roomAvailabilityThread)

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
