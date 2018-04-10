import pymongo
from pymongo import MongoClient
from  .. import database as db

_current_context=None
def get_context():
    global _current_context
    if(_current_context==None):
        client = MongoClient(
            db._config_["NO_SQL"]["HOST"],
            db._config_["NO_SQL"]["PORT"]
        )
        if (db._config_["NO_SQL"]["USER"] != ""):
            client[db._config_["NO_SQL"]["NAME"]].authenticate(db._config_["NO_SQL"]["USER"],
                                                                  db._config_["NO_SQL"]["PASSWORD"])
            _current_context = client[db._config_["NO_SQL"]["NAME"]]


    return _current_context