from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class HomePage:
    n1 ="test"
    nb_total_pages = ''
    page_index = 0
    main_page_url = "http://www.2kdb.net/players"
    Agree_button=(By.XPATH , '//button[@aria-label="AGREE"]')
    players_list = (By.XPATH ,"//td[@class='has-text-left td-position']/a")
    total_pages = (By.CSS_SELECTOR,"div.p-d-flex.p-flex-column div.layout-with-topbar div.filterbox-main div.container div.p-datatable.p-component.p-datatable-auto-layout.p-datatable-hoverable-rows.p-datatable-sm.p-datatable-gridlines.table-players:nth-child(4) div.p-paginator.p-component.p-paginator-bottom > span.p-paginator-current")


    def __init__(self,driver):
        self.driver = driver


    def OpenHomePage(self):
        self.driver.get(HomePage.main_page_url)
        self.driver.maximize_window()
        time.sleep(5)

    def getPlayersList(self):
        return self.driver.find_elements(*HomePage.players_list)


    def AgreeHandle(self):

        self.driver.find_element(*HomePage.Agree_button).click()



    def getnumberpages(self):
        self.driver.implicitly_wait(15)
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(*HomePage.total_pages).get_attribute("innerHTML")



    def previousPage(self):
        self.driver.get("https://www.2kdb.net/players#saved")

    def nextPage(self , index):
        button = self.driver.find_element_by_xpath("//button[text()=" + str(index+ 2) + "]")
        self.driver.execute_script("arguments[0].click();", button)











