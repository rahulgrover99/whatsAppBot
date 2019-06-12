from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import os
from flask import (
    flash, g, redirect, render_template, request, url_for, Flask, send_from_directory
)
app = Flask(__name__)

options = webdriver.ChromeOptions()
options.add_argument(argument="--user-data-dir="+os.path.expanduser("~")+"/.config/google-chrome")
executable_path = os.path.expanduser("~")+"/Projects/whatsAppBot/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path, options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)

#TODO make based on target
data = {"name":"Rahul","number":"+91 98143 11067","message":"Gae"}

def send_whatsapp_message(data):

    x_arg = "//span[contains(@title,'"+data["number"]+"')]"
    x_arg_name = "//span[contains(@title,'"+data["name"]+"')]"

    searBoxPath = '//*[@id="input-chatlist-search"]'

    time.sleep(10)

    # Click the search button
    try:
        driver.find_element_by_xpath("//button[contains(@class,'_1XCAr')]").click()
    except:
        pass

    inputSearchBox = driver.find_element_by_xpath("//input[contains(@title,'Search or start new chat')]")
    inputSearchBox.send_keys(data["number"])

    print('Target Searched')

    # Increase the time if searching a contact is taking a long time
    time.sleep(2)

    try:
        driver.find_element_by_xpath(x_arg).click()
    except:
        driver.find_element_by_xpath(x_arg_name).click()

    print("Target Successfully Selected")
    time.sleep(2)

    # Select the input box
    inp_xpath = "//div[@contenteditable='true']"
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    time.sleep(1)

    input_box.send_keys("Hello, " + data["name"] + "." + Keys.ENTER + data["message"])
    input_box.send_keys(Keys.ENTER)

#send_whatsapp_message(data)

@app.route("/")
def index():
    try:
        name = request.args.get('name')
        number = request.args.get('number')
        message = request.args.get('message')
        data = {"name": name, "number": number,"message": message}
        send_whatsapp_message(data)
        return render_template("index.html")
    except:

        return render_template("error.html", error=error)

if __name__ == "__main__":
    app.run()

