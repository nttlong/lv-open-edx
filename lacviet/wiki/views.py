from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.http import *
from edxmako.shortcuts import render_to_response
import MySQLdb


from xmodule.modulestore.split_mongo.mongo_connection import MongoConnection
def get_wiki(request):

    db = MySQLdb.connect(host="172.16.7.63",    # your host, usually localhost
                         port=3306,
                         user="root",         # your username
                         passwd="123456",  # your password
                         db="lv_lms")        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT created,title,content, article_id FROM wiki_articlerevision")
    data = cur.fetchall()
    columns = cur.description
    listcolumn = []
    for col in columns:
        listcolumn.append(col[0])
    result = [{columns[index][0]: column for index, column in enumerate(value)} for value in data]
    context = {
        'data': result,
        'listcolumn': listcolumn

    }
    cur.close()
    db.close()
    return render_to_response("wiki.html", context)