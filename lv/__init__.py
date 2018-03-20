import lv_utils
import uuid
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.http import *
def get_list_of_students():
    test = list(lv_utils.mongo_db()["modulestore.definitions"].aggregate([
        {
            "$project":{
                "_id":0
                ,"block_type":1
            }
        }
    ])["result"])
    return test
    #return  ["a","b","c"]
def get_user_db(param):

    if User.objects.filter(username=param["username"]).exists():
        token = str(uuid.uuid4())
        user_lg = lv_utils.mongo_db()["hcs_users"].update_one({"username":param["username"]},{"$set": {
            "token":token
        }})
        return {
            "username": param["username"],
            "token": token
        };
    else:
        #Create password in 2 bb mongodb and mysql
        passwd = str(uuid.uuid4())
        user_lg = {
            "username": param["username"],
            "token" : str(uuid.uuid4()),
            "password": passwd
        }
        #insert in db mongodb
        lv_utils.mongo_db()["hcs_users"].insert_one(user_lg)
        #insert in db mysql
        userInsert = User.objects.create_user(param["username"], param["email"], passwd)
        userInsert.save()
        return {
            "username": user_lg["username"],
            "token": user_lg["token"]
        };