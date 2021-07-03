from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

list_links =[]
list_1 = []



def Collect_player_data():
    color_list = ["bronze", "silver", "gold", "emerald", "ruby", "amethyst", "heatcheck", "pink_diamond", "diamond",
                  "galaxy_opal", "dark_matter"]
    global Name
    global Color
    global Team
    global Position
    global Speed
    global Shot_threepoint
    global Pdefense
    global Idefense
    global Passing
    global Block
    global Steal
    global Orebound
    global Drebound

    Name = driver.find_element_by_xpath('//p[@class="title is-size-4-mobile is-size-3-widescreen has-text-weight-bold has-text-white"]').get_attribute(
        "innerHTML"
    )

    imarge_source = driver.find_element_by_css_selector(
    "div.container.is-fluid.mobile-nopadding div.columns.is-mobile.is-multiline.is-player-card.mobile-padding:nth-child(1) div.column.is-full-mobile.is-full-desktop.is-full-widescreen div.columns.is-mobile.is-multiline div.column.is-full-mobile.tablet-769px.is-9-tablet.is-four-fifths-fullhd:nth-child(1) div.columns.is-mobile.is-multiline.justify-header div.column.is-full-mobile.is-8-tablet.is-player-info:nth-child(2) div.columns.is-mobile.is-multiline div.column.is-1-mobile.is-1-tablet.ovr-margin:nth-child(1) div.has-text-centered figure.image.is-48x48 > img:nth-child(1)").get_attribute(
    "src")

    for col in color_list:
        if col in imarge_source:
            Color = col
            break
    Speed = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[1]/span[1]").get_attribute(
        "innerHTML")

    Shot_threepoint = driver.find_element_by_xpath(
        "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[3]/span[1]").get_attribute("innerHTML")

    Pdefense = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/span[1]").get_attribute(
        "innerHTML")
    Idefense = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[1]").get_attribute(
        "innerHTML"
    )

    Passing = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/div[3]/span[1]").get_attribute(
        "innerHTML"
    )

    Block = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[7]/span[1]").get_attribute(
        "innerHTML"
    )
    Steal = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[7]/span[1]").get_attribute(
        "innerHTML"
    )
    Orebound = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div[1]/span[1]").get_attribute(
        "innerHTML"
    )
    Drebound = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div[2]/span[1]").get_attribute(
        "innerHTIML"
    )

    Team = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[9]/p[2]').get_attribute(
        "innerHTML"
    )
    Position = driver.find_element_by_xpath(
        '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[8]/p[2]').get_attribute(
        "innerHTML")

    return Name , Color , Team , Position , Speed , Shot_threepoint , Pdefense , Idefense , Passing , Block , Steal , \
           Orebound, Drebound





def Store_to_dataframe (Name , Color , Team , Position , Speed , Shot_threepoint , Pdefense , Idefense , Passing , Block , Steal ,
           Orebound, Drebound) :
    player_names = []
    player_teams = []
    player_positions = []
    player_speeds = []
    player_3pts = []
    player_colors = []
    player_steal = []
    player_Pdefense = []
    player_Idefense = []
    player_Block = []
    player_Orebound = []
    player_Drebound = []
    player_Passing = []

    player_names.append(Name)
    player_teams.append(Team)
    player_speeds.append(Speed)
    player_positions.append(Position)
    player_3pts.append(Shot_threepoint)
    player_colors.append(Color)
    player_steal.append(Steal)
    player_Passing.append(Passing)
    player_Drebound.append(Drebound)
    player_Orebound.append(Orebound)
    player_Pdefense.append(Pdefense)
    player_Block.append(Block)
    player_Idefense.append(Idefense)
    player_base = {"Name": player_names, "Team": player_teams, "Color": player_colors, "Position": player_positions,
                   "Speed": player_speeds, "Three_points": player_3pts, "Steal": player_steal,
                   "Passing": player_Passing,
                   "Defensive_Rebound": player_Drebound, "Offensive_Rebound": player_Orebound,
                   "Perimeter_Defense": player_Pdefense,
                   "Interior_defense": player_Idefense, "Block": player_Block}

    global player_df
    player_df = pd.DataFrame(player_base, columns=["Name", "Team", "Color", "Position", "Speed", "Three_points", "Steal",
                                                   "Passing", "Defensive_Rebound", "Offensive_Rebound", "Perimeter_Defense",
                                                   "Interior_Defense", "Block"])

    return print(player_df.head(5))



driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://www.2kdb.net/players")

driver.maximize_window()
time.sleep(5)
try:
    driver.find_element_by_xpath('//button[@aria-label="AGREE"]').click()
except:
    NoSuchElementException
pass

list_links=driver.find_elements_by_xpath("//td[@class='has-text-left td-position']/a")

for elem in list_links:
    list_1.append(elem.get_attribute("href"))

i = 0

for i in range(len(list_1)):

    driver.get(list_1[i])
    Collect_player_data()
    Store_to_dataframe(Name , Color , Team , Position , Speed , Shot_threepoint , Pdefense , Idefense , Passing , Block , Steal ,
           Orebound, Drebound)
    time.sleep(3)
    driver.back()


print(player_df.head(10))