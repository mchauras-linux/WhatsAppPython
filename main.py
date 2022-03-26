from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import string
import random
 
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('./chromedriverLinux')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Gudiya Singh"'
 
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'
print("Searching InputBox")
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
print("InputBox Found")
for i in range(1000):
    #Generate Random String
    N = 11
    # Replace the below string with your own message
    message = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = N)))
    input_box.send_keys(str("Suffer My Wrath: ") + message + Keys.ENTER)
    time.sleep(30)