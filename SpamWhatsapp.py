from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import os

#TODO make based on target

msgToSend = [12, 32, 0, "What's up!", "I am a bot!"]

targets = []

options = webdriver.ChromeOptions()
options.add_argument(argument="--user-data-dir="+os.path.expanduser("~")+"/.config/google-chrome")
executable_path = os.path.expanduser("~")+"/Projects/whatsAppBot/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path, options=options)

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)

target = "9461333355"

x_arg = '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[1]/span/span'

searBoxPath = '//*[@id="input-chatlist-search"]'

time.sleep(4)

# Click the search button
driver.find_element_by_xpath("//button[contains(@class,'_1XCAr')]").click()
# driver.find_element_by_class_name('_1XCAr').click()
# driver.find_element_by_css_selector('button._1XCAr').click()

inputSearchBox = driver.find_element_by_xpath("//input[contains(@title,'Search or start new chat')]")
inputSearchBox.send_keys(target)

print('Target Searched')
# Increase the time if searching a contact is taking a long time
time.sleep(2)

driver.find_element_by_xpath(x_arg).click()
print("Target Successfully Selected")
time.sleep(2)
'''
# Select the input box
inp_xpath = "//div[@contenteditable='true']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
time.sleep(1)

for i in range(0,2):
    input_box.send_keys("Hello, " + target + "."+ Keys.SHIFT + Keys.ENTER + msgToSend[3])
    input_box.send_keys(Keys.ENTER)
    input_box.send_keys(msgToSend[4])
    input_box.send_keys(Keys.ENTER) 

time.sleep(5)
print("Successfully Send Message to : "+ target + '\n')
time.sleep(0.5)

'''


