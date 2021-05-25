import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
color_list= ["bronze", "silver", "gold" ,"emerald","ruby","amethyst","heatcheck", "pink_diamond","diamond","galaxy_opal","dark_matter"]
player_names = []
player_teams = []
player_positions =[]
player_speeds =[]
player_3pts = []
player_colors =[]

root = tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)


root.mainloop()

def find_player():
    x1 = entry1.get()

    driver.get("http://www.2kdb.net")

    driver.implicitly_wait(15)
    try:
        driver.find_element_by_css_selector("#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-1tbbj19").click()
    except : NoSuchElementException
    pass


    #search_for_player
    driver.find_element_by_tag_name("input").send_keys(x1)
    driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)


    #gather player data
    imarge_source =driver.find_element_by_css_selector("div.container.is-fluid.mobile-nopadding div.columns.is-mobile.is-multiline.is-player-card.mobile-padding:nth-child(1) div.column.is-full-mobile.is-full-desktop.is-full-widescreen div.columns.is-mobile.is-multiline div.column.is-full-mobile.tablet-769px.is-9-tablet.is-four-fifths-fullhd:nth-child(1) div.columns.is-mobile.is-multiline.justify-header div.column.is-full-mobile.is-8-tablet.is-player-info:nth-child(2) div.columns.is-mobile.is-multiline div.column.is-1-mobile.is-1-tablet.ovr-margin:nth-child(1) div.has-text-centered figure.image.is-48x48 > img:nth-child(1)").get_attribute("src")

    for col in color_list :
        if col in imarge_source :
            color = col
            break


    Speed = driver.find_element_by_xpath("//body/div[@id='__next']/div[2]/div[3]/div[2]/div[1]/div[1]/span[1]").get_attribute("innerHTML")

    Shoot_threepoint = driver.find_element_by_xpath("//body/div[@id='__next']/div[2]/div[3]/div[1]/div[1]/div[3]/span[1]").get_attribute("innerHTML")

    Position = driver.find_element_by_xpath("//body/div[@id='__next']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[8]/p[2]").get_attribute("innerHTML")
    Team = driver.find_element_by_css_selector("div.container.is-fluid.mobile-nopadding div.columns.is-mobile.is-multiline.is-player-card.mobile-padding:nth-child(1) div.column.is-full-mobile.is-full-desktop.is-full-widescreen div.columns.is-mobile.is-multiline div.column.is-full-mobile.tablet-769px.is-9-tablet.is-four-fifths-fullhd:nth-child(1) div.columns.is-mobile.is-multiline.justify-header div.column.is-full-mobile.is-8-tablet.is-player-info:nth-child(2) div.columns.is-mobile.is-multiline div.column.is-half-mobile.is-2-tablet.info-columns-tablet:nth-child(9) > p.title.is-size-6.has-text-white.line-clamp").get_attribute("innerHTML")
    driver.close()
    player_names.append(x1)
    player_teams.append(Team)
    player_speeds.append(Speed)
    player_positions.append(Position)
    player_3pts.append(Shoot_threepoint)
    player_colors.append(color)



    player_base ={ "Name" : player_names , "Team" : player_teams,"Color" :player_colors  ,"Position" : player_positions ,"Speed" : player_speeds, "3pt" : player_3pts}

    player_df = pd.DataFrame(player_base , columns=["Name" , "Team" ,"Color","Position" ,"Speed","3pt"])


    print(player_df.head(5))



button1 = tk.Button(text='find player', command=find_player())
canvas1.create_window(200, 180, window=button1)
root.mainloop()

