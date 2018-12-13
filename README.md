# MeetingRoom
A program written in Python 3.x, HTML, CSS and JavaScript to work as a monitor outside a meeting room showing today's meetings, and also allows you to book meetings right there on the screen. This is based on Microsoft Exchange.

### Intended use

This is intended to be used on a Raspberry Pi 2/3 with the 7" touch screen monitor inside a case mounted on the wall.

### Prerequisites

This application uses the Eel module for Python which allows you to design UI with HTML and CSS, and to use JavaScript and Python functions to pass information betweeen Python and the GUI.
Other dependencies are the python modules exchangelib and datetime.

```
pip install eel exchangelib datetime
```

### Work in progress

So far what's everything in the Python script that reads and writes to Microsoft Exchange is working.

![Meeting01](https://github.com/Myrheimb/MeetingRoom/blob/master/Images/Meeting01.png)
![Meeting02](https://github.com/Myrheimb/MeetingRoom/blob/master/Images/Meeting02.png)

The current work is being done on designing the UI, and the next step will be to pass the needed information and functionality between Python and the UI. See the current UI layout here for Vacant and Occupied status.

![Vacant](https://github.com/Myrheimb/MeetingRoom/blob/master/Images/Vacant.png)
![Occupied](https://github.com/Myrheimb/MeetingRoom/blob/master/Images/Occupied.png)
