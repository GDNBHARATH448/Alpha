import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27639080")) #optional
API_HASH = getenv("API_HASH", "5c10faa5b68227793d5f9084106c6f24") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7403621976").split()))
OWNER_ID = int(getenv("OWNER_ID", "8187405882"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "7789341824:AAFVRNcPZq0oVfmDnVGHhZWlRQ9nHhc2GRM")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/889eb69b32f94476bc712-9558bff09cbd6faaf6.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMPURVI/ALPHA_USERBOT")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGlvSgAJWi2yfIs0zvrE2bZW4Q3TtYSoZTmcMgUJjdaUB9Rkq65b0JzwXqiBcVzNiQhavgdnNAYZAYAvkgkSQ0bt6udlwdkMraHPJD7NY7yECvBBJ2FFFMoAsKsBZOFjW3GqIwRWslvNSmCi99yxBDUdPXOG6D_35rLwSHhAgiNWJe0sUNkTtYP3iCemwb9I4dv2xAbTU2z3Wj6Y4j7i-ZqjFJhvX0gJtgiM8kR02dVUof_iBdCxoiF9uZJ739XH4QIHI8OVRfLm04EoYi75hVPwQQq8Zwq9tE0YmXPBlvDR80slwxNxiDGH-vN2HQFWlfzMIEowBLKqjmzqceafnfGSfP1HAAAAAHoAeY6AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
