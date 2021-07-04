import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

list_links=[]

while True:
    player = str(input("Please enter the player's name (Enter Exit to end input) :"))
    if player == "Exit":
        break
    #open_website
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    driver.get("http://www.2kdb.net")
    driver.maximize_window()
    driver.implicitly_wait(15)

    try:
        driver.find_element_by_xpath('//button[@aria-label="AGREE"]').click()
    except : NoSuchElementException
    pass
    driver.find_element_by_tag_name("input").send_keys(player)
    time.sleep(2)
    list= driver.find_elements_by_xpath('//li//a[@class="navsearch-link"]')
    for card in list:
        print(card.get_attribute("href"))
        list_links.append(card.get_attribute("href"))

    driver.get(list_links[1])

