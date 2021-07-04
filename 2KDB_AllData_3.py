from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import PlayerPage
from PlayerPage import PlayerPage


list_1 = []
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

    driver.implicitly_wait(15)

    playerPage = PlayerPage(driver)

    Name = playerPage.getPlayerName()

    Image_player = playerPage.getPlayerImage()

    for col in color_list:
        if col in Image_player:
            Color = col
            break
    Speed = playerPage.getPlayerSpeed()

    Shot_threepoint = playerPage.getPlayerShothreepts()

    Pdefense = playerPage.getPlayerPDefense()

    Idefense = playerPage.getPlayerIDefense()

    Passing = playerPage.getPlayerPassing()

    Block = playerPage.getPlayerBlock()

    Steal = playerPage.getPlayerSteal()

    Orebound = playerPage.getPlayerOrebound()

    Drebound = playerPage.getPlayerDrebound()

    Team = playerPage.getPlayerTeam()

    Position = playerPage.getPlayerPosition()

    return Name , Color , Team , Position , Speed , Shot_threepoint , Pdefense , Idefense , Passing , Block , Steal , \
           Orebound, Drebound




driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://www.2kdb.net/players")

driver.maximize_window()
time.sleep(5)
try:
    driver.find_element_by_xpath('//button[@aria-label="AGREE"]').click()
except:
    NoSuchElementException
pass

for j in range(2):


    list_links = driver.find_elements_by_xpath("//td[@class='has-text-left td-position']/a")

    for elem in list_links:
        list_1.append(elem.get_attribute("href"))

    for i in range(len(list_1)):

        driver.get(list_1[i])
        Collect_player_data()
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
        time.sleep(3)


    driver.get("https://www.2kdb.net/players#saved")
    button = driver.find_element_by_xpath("//button[text()="+str(j+2)+"]")
    driver.execute_script("arguments[0].click();", button)
    list_1=[]
    time.sleep(3)



player_base = {"Name": player_names, "Team": player_teams, "Color": player_colors, "Position": player_positions,
                   "Speed": player_speeds, "Three_points": player_3pts, "Steal": player_steal,
                   "Passing": player_Passing,
                   "Defensive_Rebound": player_Drebound, "Offensive_Rebound": player_Orebound,
                   "Perimeter_Defense": player_Pdefense,
                   "Interior_defense": player_Idefense, "Block": player_Block}

player_df = pd.DataFrame(player_base, columns=["Name", "Team", "Color", "Position", "Speed", "Three_points", "Steal",
                                             "Passing", "Defensive_Rebound", "Offensive_Rebound", "Perimeter_Defense",
                                             "Interior_Defense", "Block"])

player_df.to_csv('test.csv')

print(player_df.head(5))
