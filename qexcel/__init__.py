
_coll_language = None
_coll_error = None
_db = None
def set_config(host,port,db,user,password):
    global _coll_language
    global _db
    global _coll_error
    from pymongo import mongo_client

    cnn = mongo_client.MongoClient(host=host, port=port)
    _db = cnn.get_database(db)
    _db.authenticate(user, password)
    _coll_language = _db.get_collection("sys.export_import_language")
    _coll_error = _db.get_collection("sys.export_import_error")



    pass
def get_coll_language():
    global _coll_language
    global _db
    global _coll_error
    if _coll_language == None:
        from django.conf import settings
        host = settings.DOC_STORE_CONFIG["host"]
        port = settings.DOC_STORE_CONFIG["port"]
        db = settings.DOC_STORE_CONFIG["db"]
        user = settings.DOC_STORE_CONFIG["user"]
        password = settings.DOC_STORE_CONFIG["password"]
        set_config(host,port,db,user,password)
    return _coll_language
        


    return _coll_language
def get_coll_error():
    global _coll_language
    global _db
    global _coll_error
    if _coll_language == None:
        from django.conf import settings
        host = settings.DOC_STORE_CONFIG["host"]
        port = settings.DOC_STORE_CONFIG["port"]
        db = settings.DOC_STORE_CONFIG["db"]
        user = settings.DOC_STORE_CONFIG["user"]
        password = settings.DOC_STORE_CONFIG["password"]
        set_config(host, port, db, user, password)
    return _coll_error
def get_error(id):
    from django.http import HttpResponse
    import openpyxl
    from io import BytesIO
    from bson import ObjectId
    items =list(get_coll_error().find({"_id": ObjectId(id)}))
    data = items[0]["data"]
    bff = "".join(map(chr, data))
    wb = None
    with open('text','r+w') as f:
        f.write(bff)
        wb = openpyxl.load_workbook(filename=f)

    from openpyxl.writer.excel import save_virtual_workbook
    response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename= "{}"'.format("users.xlsx")
    return response

    return data



