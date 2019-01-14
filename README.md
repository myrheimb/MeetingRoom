# MeetingRoom
A program written in Python 3.x, HTML, CSS and JavaScript to work as a monitor outside a meeting room showing today's meetings. It also allows you to book meetings right there on the screen. This is based on Microsoft Exchange, but it can also be used for Office 365, but I haven't had the access to test that yet.

### Usage

This is intended to be used on a Raspberry Pi 2/3 with the 7" touch screen monitor inside a case mounted on the wall.
The program is run by adding your settings in the config.py file and starting the server.py file which opens a web browser with the GUI.

### Prerequisites

This application uses the Eel module for Python which allows you to design GUI with HTML and CSS, and to use JavaScript and Python functions to pass information betweeen Python and the GUI.
Other dependencies are the python modules exchangelib which allows you to communicate with Microsoft Exchange, and datetime.

```
pip install eel exchangelib datetime
```

Updated pictures with the GUI and functionality to come soon!
