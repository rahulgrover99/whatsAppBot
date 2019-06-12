# Whats App Bot
This is a simple Web WhatsApp Bot developed in python using Selenium. 
Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

# Features!

  - Send a specific message to a particular contact at any time of the day
  - One can send a single message to multiple contacts over a specific time
  - Multiple messages to multiple contacts
  - It offers a delay so that WhatsApp can detect your are sending a URL and show its pop-up description.
  - It can search a contact from the list if the contact isn't present in the recent chats
  - Change the message along with time in the mainBot.py
  - You can add multiple messages
  - The Script can also search for the contact in the new chat list and then send message if the contact is not found in the recent chat list.
  
### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* [openpyxl](https://pypi.org/project/openpyxl/) - To read xls files

### Installation

Step 1: Install Selenium 
```sh
$ pip3 install selenium
```

Step 2: Selenium requires a driver to interface with the chosen browser.
> [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)<br/>
> [Click for FireFox](https://github.com/mozilla/geckodriver/releases)<br/>
> [Click for safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)<br/>

Step 3: Extract the downloaded driver onto a folder

Step 4: Set path variable to the environment. Paste this command to the terminal
```sh
$ export PATH=$PATH:/home/path/to/the/driver/folder/
Eg: $ export PATH=$PATH:/home/harshit/Desktop/WhatsAppBot
```
Step 5: run mainBot.py using Python3
```sh
$ python3 mainBot.py
```
