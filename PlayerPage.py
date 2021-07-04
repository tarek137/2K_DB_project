from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


class PlayerPage:

    ob_Name = (By.XPATH,'//p[@class="title is-size-4-mobile is-size-3-widescreen has-text-weight-bold has-text-white"]')
    ob_imarge_source =(By.CSS_SELECTOR ,"div.container.is-fluid.mobile-nopadding div.columns.is-mobile.is-multiline.is-player-card.mobile-padding:nth-child(1) div.column.is-full-mobile.is-full-desktop.is-full-widescreen div.columns.is-mobile.is-multiline div.column.is-full-mobile.tablet-769px.is-9-tablet.is-four-fifths-fullhd:nth-child(1) div.columns.is-mobile.is-multiline.justify-header div.column.is-full-mobile.is-8-tablet.is-player-info:nth-child(2) div.columns.is-mobile.is-multiline div.column.is-1-mobile.is-1-tablet.ovr-margin:nth-child(1) div.has-text-centered figure.image.is-48x48 > img:nth-child(1)")
    ob_Speed = (By.XPATH,"//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[1]/span[1]")
    ob_Shot_threepoint =(By.XPATH,"//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[3]/span[1]")
    ob_Pdefense=(By.XPATH,"//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/span[1]")
    ob_Idefense=(By.XPATH,"//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[1]")
    ob_Passing = (By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/div[3]/span[1]")
    ob_Block = (By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[7]/span[1]")
    ob_Steal = (By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[7]/span[1]")
    ob_Orebound =(By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div[1]/span[1]")
    ob_Drebound =(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div[2]/span[1]")
    ob_Team =(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[9]/p[2]')
    ob_Position =(By.XPATH , '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[8]/p[2]')


    def __init__(self,driver):
        self.driver = driver

    #find  player Name
    def getPlayerName(self):
        self.driver.implicitly_wait(15)
        try:
            Name = self.driver.find_element(*PlayerPage.ob_Name).get_attribute("innerHTML")
            return Name
        except: StaleElementReferenceException
        self.driver.refresh()
        Name = self.driver.find_element(*PlayerPage.ob_Name).get_attribute("innerHTML")
        return Name



    #find player card color based on the link of the image logo
    def getPlayerImage(self):
        Image_player = self.driver.find_element(*PlayerPage.ob_imarge_source).get_attribute("src")
        return Image_player

    #find player speed attribute
    def getPlayerSpeed(self):
        Speed = self.driver.find_element(*PlayerPage.ob_Speed).get_attribute("innerHTML")
        return Speed
    #find player three points rating
    def getPlayerShothreepts(self):
        Shotthreepts = self.driver.find_element(*PlayerPage.ob_Shot_threepoint).get_attribute("innerHTML")
        return Shotthreepts

    #find player perimeter defense
    def getPlayerPDefense(self):
        PDefense = self.driver.find_element(*PlayerPage.ob_Pdefense).get_attribute("innerHTML")
        return PDefense

    #find player Interior defense
    def getPlayerIDefense(self):
        IDefense = self.driver.find_element(*PlayerPage.ob_Idefense).get_attribute("innerHTML")
        return IDefense

    #find player passing attribute
    def getPlayerPassing(self):
        Passing = self.driver.find_element(*PlayerPage.ob_Passing).get_attribute("innerHTML")
        return Passing

    #find player Blcok attribute
    def getPlayerBlock(self):
        Block =  self.driver.find_element(*PlayerPage.ob_Block).get_attribute("innerHTML")
        return Block

    #find player steal attribute
    def getPlayerSteal(self):
        Steal = self.driver.find_element(*PlayerPage.ob_Steal).get_attribute("innerHTML")
        return Steal

    #find Offensive rebound attribute
    def getPlayerOrebound(self):
        Orebound =self.driver.find_element(*PlayerPage.ob_Orebound).get_attribute("innerHTML")
        return Orebound

    #find defensive rebound attribute
    def getPlayerDrebound(self):
        Drebound = self.driver.find_element(*PlayerPage.ob_Drebound).get_attribute("innerHTML")
        return Drebound

    #find player's team
    def getPlayerTeam(self):
        Team = self.driver.find_element(*PlayerPage.ob_Team).get_attribute("innerHTML")
        return Team

    #find player position
    def getPlayerPosition(self):
        Position = self.driver.find_element(*PlayerPage.ob_Position).get_attribute("innerHTML")
        return Position




