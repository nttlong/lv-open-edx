import pymongo
from pymongo import MongoClient
from path import Path as path
import MySQLdb
import os
import json
current_db=None
db_config=None
def mongo_db():
    global current_db
    if(current_db==None):
        PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /edx-platform/cms
        REPO_ROOT = PROJECT_ROOT.dirname()
        ENV_ROOT = REPO_ROOT.dirname()
        SERVICE_VARIANT = os.environ.get('SERVICE_VARIANT', None)
        CONFIG_PREFIX = SERVICE_VARIANT + "." if SERVICE_VARIANT else ""
        CONFIG_ROOT = path(os.environ.get('CONFIG_ROOT', ENV_ROOT))
        with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
            AUTH_TOKENS = json.load(auth_file)
            client = MongoClient(
                AUTH_TOKENS.get("MONGODB_CONFIG").get("HOST"),
                int(AUTH_TOKENS.get("MONGODB_CONFIG").get("PORT"))
            )
            if(AUTH_TOKENS.get("MONGODB_CONFIG").get("USER") != ""):
                client[AUTH_TOKENS.get("MONGODB_CONFIG").get("NAME")].authenticate(AUTH_TOKENS.get("MONGODB_CONFIG").get("USER"), AUTH_TOKENS.get("MONGODB_CONFIG").get("PASSWORD"))
            current_db=client[AUTH_TOKENS.get("MONGODB_CONFIG").get("NAME")]

    return current_db
def sql_db():
    global db_config
    if(db_config==None):
        PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /edx-platform/cms
        REPO_ROOT = PROJECT_ROOT.dirname()
        ENV_ROOT = REPO_ROOT.dirname()
        SERVICE_VARIANT = os.environ.get('SERVICE_VARIANT', None)
        CONFIG_PREFIX = SERVICE_VARIANT + "." if SERVICE_VARIANT else ""
        CONFIG_ROOT = path(os.environ.get('CONFIG_ROOT', ENV_ROOT))
        with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
            AUTH_TOKENS = json.load(auth_file)
            db_config={
                "name":AUTH_TOKENS.get("MYSQL_CONFIG").get("NAME"),
                "host":AUTH_TOKENS.get("MYSQL_CONFIG").get("HOST"),
                "user": AUTH_TOKENS.get("MYSQL_CONFIG").get("USER"),
                "password": AUTH_TOKENS.get("MYSQL_CONFIG").get("PASSWORD")
            }



