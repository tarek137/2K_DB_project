from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

list1 = []
list2 = []
list3 =[]
color_list= ["bronze", "silver", "gold" ,"emerald","ruby","amethyst","heatcheck", "pink_diamond","diamond","galaxy_opal","dark_matter"]

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://www.2kdb.net/players")
driver.implicitly_wait(15)
driver.maximize_window()
time.sleep(5)
try:
        driver.find_element_by_xpath('//button[@aria-label="AGREE"]').click()

except :
    NoSuchElementException
pass
driver.refresh()

button = driver.find_element_by_css_selector("div.p-d-flex.p-flex-column div.layout-with-topbar div.filterbox-main div.container div.p-datatable.p-component.p-datatable-auto-layout.p-datatable-hoverable-rows.p-datatable-sm.p-datatable-gridlines.table-players:nth-child(4) div.p-paginator.p-component.p-paginator-bottom > span.p-paginator-current").get_attribute("innerHTML")

print(button[-4:-1])












