import pymongo
from pymongo import MongoClient
from path import Path as path
import  configs
import MySQLdb
import os
import json
import  sys
from lv_utils import  configs

current_db=None
db_config=None
def mongo_db():
    global current_db
    if(current_db==None):
        client = MongoClient(
            configs.get_config().no_sql.host,
            configs.get_config().no_sql.port
        )
        if (configs.get_config().no_sql.user != ""):
            client[configs.get_config().no_sql.name].authenticate(configs.get_config().no_sql.user,
                                                                  configs.get_config().no_sql.password)
        current_db = client[configs.get_config().no_sql.name]


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
def configuration():
    return  configs()


