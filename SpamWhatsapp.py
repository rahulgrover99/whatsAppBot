from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import datetime
import time
import openpyxl as excel
import os
from flask import (
    flash, g, redirect, render_template, request, url_for, Flask, send_from_directory
)

app = Flask(__name__)

os.environ['MOZ_HEADLESS'] = '1'

#binary = FirefoxBinary('/home/aviwad/Projects/whatsAppBot/geckodriver')
driver = webdriver.Firefox(executable_path='/home/ubuntu/RahulGrover/geckodriver')
#options = webdriver.ChromeOptions()
#options.add_argument(argument="--kiosk")
#options.add_argument(argument='--window-size=1366x768');
#options.add_argument(argument="--start-maximized")
#options.add_argument(argument="--user-data-dir="+os.path.expanduser("~")+"/.config/google-chrome")
#executable_path = os.path.expanduser("~")+"/Projects/whatsAppBot/chromedriver_linux64/chromedriver"
#driver = webdriver.Chrome(executable_path=executable_path, options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)

def send_whatsapp_message(data):

    x_arg = "//span[contains(@title,'"+data["number"]+"')]"
    x_arg_name = "//span[contains(@title,'"+data["name"]+"')]"

    # searBoxPath = '//*[@id="input-chatlist-search"]'
    time.sleep(10)

    # Click the search button
    try:
        driver.find_element_by_xpath("//button[contains(@class,'_1XCAr')]").click()
    except:
        print("Search button not found! Check xpath")
        pass

    inputSearchBox = driver.find_element_by_xpath("//input[contains(@title,'Search or start new chat')]")
    inputSearchBox.send_keys(data["number"])

    print('Target Searched')

    # Increase the time if searching a contact is taking a long time
    time.sleep(2)

    # Finding the contact
    try:
        driver.find_element_by_xpath(x_arg).click()
        print('number clicked')
    except:
        driver.find_element_by_xpath(x_arg_name).click()
        print('group clicked')

    print("Target Successfully Selected")
    time.sleep(2)

    # Select the input box
    '''
    inp_xpath = "//div[@contenteditable='true']"
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    time.sleep(1)

    input_box.send_keys("Hello, " + data["name"] + "." + Keys.ENTER + data["message"])
    input_box.send_keys(Keys.ENTER)
    for i in range(int(data["loopnumber"])):
        input_box.send_keys(data["message"])
        input_box.send_keys(Keys.ENTER)
    '''

time=time.time()
#send_whatsapp_message(data)
@app.route("/qr")
def qrcode():
    save_screenshot()
    return render_template("screenshot.html",time=time)

def save_screenshot():
    try:
        os.rm("static/screenshot.png")
    except:
        pass
    driver.save_screenshot("static/screenshot.png")

@app.route("/")
def index():
    try:
        name = request.args.get('name')
        number = request.args.get('number')
        message = request.args.get('message')
        loopnumber = request.args.get('loopnumber')
        data = {"name": name, "number": number,"message": message,"loopnumber":loopnumber}
        send_whatsapp_message(data)
        return render_template("index.html")
    except:
        error = "missing argument (name, number, or message), check if QR scan scene is present"
        save_screenshot()
        return render_template("error.html", error=error, time=time)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="6969")

