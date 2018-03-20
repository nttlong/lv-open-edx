import pymongo
from pymongo import MongoClient
from path import Path as path
import os
import json
current_db=None
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
            # AUTH_TOKENS.get("DATABASES").get("default").update({"NAME": AUTH_TOKENS.get("MYSQL_CONFIG").get("NAME")})
            # AUTH_TOKENS.get("DATABASES").get("default").update({"HOST": AUTH_TOKENS.get("MYSQL_CONFIG").get("HOST")})
            # AUTH_TOKENS.get("DATABASES").get("default").update({"USER": AUTH_TOKENS.get("MYSQL_CONFIG").get("USER")})
            # AUTH_TOKENS.get("DATABASES").get("default").update(
            #     {"PASSWORD": AUTH_TOKENS.get("MYSQL_CONFIG").get("PASSWORD")})
            # AUTH_TOKENS.get("DATABASES").get("default").update({"PORT": AUTH_TOKENS.get("MYSQL_CONFIG").get("PORT")})
            client = MongoClient(
                AUTH_TOKENS.get("MONGODB_CONFIG").get("HOST"),
                int(AUTH_TOKENS.get("MONGODB_CONFIG").get("PORT"))
            )
            if(AUTH_TOKENS.get("MONGODB_CONFIG").get("USER") != ""):
                client[AUTH_TOKENS.get("MONGODB_CONFIG").get("NAME")].authenticate(AUTH_TOKENS.get("MONGODB_CONFIG").get("USER"), AUTH_TOKENS.get("MONGODB_CONFIG").get("PASSWORD"))
            current_db=client[AUTH_TOKENS.get("MONGODB_CONFIG").get("NAME")]

    return current_db

