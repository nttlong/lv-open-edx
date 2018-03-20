import lv_utils
def get_list_of_students():
    test = list(lv_utils.mongo_db()["modulestore.definitions"].aggregate([
        {
            "$project":{
                "_id":0
                ,"block_type":1
            }
        }
    ]))
    return test
    #return  ["a","b","c"]