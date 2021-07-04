import PlayerPage
from PlayerPage import PlayerPage
import pandas as pd
import sqlalchemy
import urllib





class Data:

    Name =''
    Color =''
    Team =''
    Position =''
    Speed =''
    Shot_threepoint =''
    Pdefense = ''
    Idefense = ''
    Passing = ''
    Block = ''
    Steal = ''
    Orebound = ''
    Drebound = ''
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
    player_base ={}
    player_df= None

    def __init__(self, driver):
        self.driver = driver

    def Collect_player_data(self):
        color_list = ["bronze", "silver", "gold", "emerald", "ruby", "amethyst", "heatcheck", "pink_diamond", "diamond",
                  "galaxy_opal", "dark_matter"]



        self.driver.implicitly_wait(15)

        playerPage = PlayerPage(self.driver)

        Data.Name= playerPage.getPlayerName()

        Data.Image_player = playerPage.getPlayerImage()

        for col in color_list:
            if col in Data.Image_player:
                Data.Color = col
                break
        Data.Speed = playerPage.getPlayerSpeed()

        Data.Shot_threepoint = playerPage.getPlayerShothreepts()

        Data.Pdefense = playerPage.getPlayerPDefense()

        Data.Idefense = playerPage.getPlayerIDefense()

        Data.Passing = playerPage.getPlayerPassing()

        Data.Block = playerPage.getPlayerBlock()

        Data.Steal = playerPage.getPlayerSteal()

        Data.Orebound = playerPage.getPlayerOrebound()

        Data.Drebound = playerPage.getPlayerDrebound()

        Data.Team = playerPage.getPlayerTeam()

        Data.Position = playerPage.getPlayerPosition()

        return Data.Name , Data.Color , Data.Team , Data.Position , Data.Speed , Data.Shot_threepoint , Data.Pdefense , Data.Idefense , Data.Passing , Data.Block , Data.Steal , \
           Data.Orebound, Data.Drebound

    #storing player attributes in lists
    def Process_Data ( self , Name, Color ,Team , Position , Speed , Shot_threepoint ,
        Pdefense  , Idefense , Passing , Block, Steal  ,Orebound , Drebound ) :

            Data.player_names.append(Name)
            Data.player_teams.append(Team)
            Data.player_speeds.append(Speed)
            Data.player_positions.append(Position)
            Data.player_3pts.append(Shot_threepoint)
            Data.player_colors.append(Color)
            Data.player_steal.append(Steal)
            Data.player_Passing.append(Passing)
            Data.player_Drebound.append(Drebound)
            Data.player_Orebound.append(Orebound)
            Data.player_Pdefense.append(Pdefense)
            Data.player_Block.append(Block)
            Data.player_Idefense.append(Idefense)

            return Data.player_names , Data.player_teams , Data.player_speeds , Data.player_positions , Data.player_3pts ,\
            Data.player_colors ,Data.player_steal,Data.player_Passing,Data.player_Drebound,Data.player_Orebound,\
            Data.player_Pdefense, Data.player_Block, Data.player_Idefense

    #collected data is stored in a dictionary of lists before being converted into dataframe
    def Store_dataframe(self):

        Data.player_base = {"Name": Data.player_names, "Team": Data.player_teams, "Color": Data.player_colors,
                       "Position": Data.player_positions,
                       "Speed": Data.player_speeds, "Three_points": Data.player_3pts, "Steal": Data.player_steal,
                       "Passing": Data.player_Passing,
                       "Defensive_Rebound": Data.player_Drebound, "Offensive_Rebound": Data.player_Orebound,
                       "Perimeter_Defense": Data.player_Pdefense,
                       "Interior_defense": Data.player_Idefense, "Block_rate": Data.player_Block}

        Data.player_df = pd.DataFrame(Data.player_base, columns=["Name", "Team", "Color", "Position", "Speed", "Three_points", "Steal",
                                             "Passing", "Defensive_Rebound", "Offensive_Rebound", "Perimeter_Defense",
                                             "Interior_Defense", "Block_rate"])

        return  Data.player_df

    #sending data to local MS SQL server database
    def transfer_to_database(self):

        quoted = urllib.parse.quote_plus('Driver={SQL Server};'
                                         'Server=LAPTOP-D9IVA0RT;'
                                         'Database=2K_DB;'
                                         'Trusted_Connection=yes;')
        engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

        Data.player_df.to_sql("Players", engine, if_exists='append')

