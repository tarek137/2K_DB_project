import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime , date


driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://www.2kdb.net")
driver.implicitly_wait(15)
driver.maximize_window()
time.sleep(5)
try:
        driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
except : NoSuchElementException
pass

driver.find_element_by_xpath("//a[contains(text(),'Updates')]").click()

date1 = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[3]/div[1]/nav[1]/div[1]/a[1]/span[1]/span[1]").get_attribute("innerHTML")

print(date1)

today = date.today()
d1 = today.strftime('%m-%d-%Y')
print(d1)

if (d1 == date1):

    print("it is ok for an update")
