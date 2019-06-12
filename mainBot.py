# Keep all contacts unique
# Can save contact with their phone Number

# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import os

msgToSend = [12, 32, 0, "Muh me le", "Gaandu"]
# Driver to open a browser
options = webdriver.ChromeOptions()
options.add_argument(argument="--user-data-dir="+os.path.expanduser("~")+"/.config/google-chrome")
executable_path = os.path.expanduser("~")+"/Projects/whatsAppBot/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path, options=options)


#link to open a site
driver.get("https://web.whatsapp.com/")

# 10 sec wait time to load, if good internet connection is not good then increase the time
# units in seconds
# note this time is being used below also
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)
target = "Gurgaon Archit"
#TODO make based on target
x_arg = "//span[contains(@title,'"+target+"')]"

#wait5.until(EC.presence_of_element_located((
#    By.XPATH, x_arg
#)))
#try:
# Select the target
#x_arg = '//span[contains(@title,' + target + ')]'
# If contact not found, then search for it
searBoxPath = '//*[@id="input-chatlist-search"]'

time.sleep(0.5)
# click the search button
time.sleep(5)
driver.find_element_by_xpath("//button[contains(@class,'_1XCAr')]").click()
inputSearchBox = driver.find_element_by_xpath("//input[contains(@title,'Search or start new chat')]")
inputSearchBox.send_keys(target)
print('Target Searched')
# Increase the time if searching a contact is taking a long time
time.sleep(5)

driver.find_element_by_xpath(x_arg).click()
print("Target Successfully Selected")
time.sleep(2)

# Select the Input Box
inp_xpath = "//div[@contenteditable='true']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
time.sleep(1)

# Send message
# taeget is your target Name and msgToSend is you message
for i in range(0,10):
    input_box.send_keys("Hello, " + target + "."+ Keys.SHIFT + Keys.ENTER + msgToSend[3])
    input_box.send_keys(Keys.ENTER)
    input_box.send_keys(msgToSend[4])
    input_box.send_keys(Keys.ENTER)  # + Keys.ENTER (Uncomment it if your msg doesnt contain '\n')
# Link Preview Time, Reduce this time, if internet connection is Good
time.sleep(10)
print("Successfully Send Message to : "+ target + '\n')
success+=1
time.sleep(0.5)

#except:
#    print("LOL")

#inp_xpath = "//div[@contenteditable='true']"
#input_box = wait.until(EC.presence_of_element_located((
#By.XPATH, inp_xpath)))


