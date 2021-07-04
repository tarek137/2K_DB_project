from selenium import webdriver
import time
from Data import Data
from HomePage import HomePage
from tqdm import tqdm
from selenium.common.exceptions import TimeoutException

players_links = []

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
homePage = HomePage(driver)
data = Data(driver)

homePage.OpenHomePage()

homePage.AgreeHandle()

nb = int(homePage.getnumberpages()[-4:-1])

for j in tqdm(range(nb)):


    players_list = homePage.getPlayersList()

    for link in players_list:
        players_links.append(link.get_attribute("href"))

    for i in range(len(players_links)):
        try:
            driver.get(players_links[i])
        except: TimeoutException
        driver.refresh()
        driver.get(players_links[i])


        data.Collect_player_data()
        data.Process_Data(data.Name, data.Color ,data.Team , data.Position , data.Speed , data.Shot_threepoint ,
                          data.Pdefense,data.Idefense , data.Passing , data.Block, data.Steal ,data.Orebound ,
                          data.Drebound)

        time.sleep(3)

    homePage.previousPage()
    homePage.nextPage(j)
    players_links =[]
    print("Page "+str(j)+" done")
    time.sleep(3)


data.Store_dataframe()

data.player_df.to_csv('test.csv')

print(data.player_df.head(5))

data.transfer_to_database()

driver.close()
