from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import string
import random

driver = webdriver.Chrome('./chromedriverLinux')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Manisha"'
 
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'
print("Searching InputBox")
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
print("InputBox Found")
for i in range(100):
    # Replace the below string with your own message
    message = str("Message ") + str(i) + str(": I wrote code for spamming Whatsapp. Gudiya Challenged me. Suffer my Wrath now :D")

    #Generate Random String
    #message = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 11)))
    print("Message number: " + str(i))
    input_box.send_keys( message + Keys.ENTER)
    time.sleep(1)