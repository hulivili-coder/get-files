import os

# Bot configuration settings
class Config:
    def __init__(self):
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.PREFIX = "E!"
        self.OWNER_IDS = [1300838678280671264, 1382187068373074001]  # Replace with actual owner IDs
        self.DB_PATH = "eventus.db"  # Path to your database

config = Config()
