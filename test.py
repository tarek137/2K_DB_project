from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

list1 = []
list2 = []
list3 =[]
color_list= ["bronze", "silver", "gold" ,"emerald","ruby","amethyst","heatcheck", "pink_diamond","diamond","galaxy_opal","dark_matter"]

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

driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[3]/div[1]/nav[1]/div[1]/a[1]/span[1]/span[1]").click()


time.sleep(5)

list1 = driver.find_elements_by_tag_name("a")

for val in list1 :
    list2.append(val.get_attribute("href"))

for i in range(len(list2)):
    if "player/2k21" in str(list2[i]):
        list3.append(list2[i])
    else :
        continue

for i in range(len(list3)):
    driver.get(list3[i])
    time.sleep(5)
    driver.back()

driver.close()










