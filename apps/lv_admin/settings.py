# -*- coding: utf-8 -*-
name="lv_admin"
is_public=True
import qexcel
login_url = "login"
def authenticate(request):
    user = request.user
    is_not_ok = user == None or user.is_anonymous() or user.is_superuser == False or user.is_active == False
    return not is_not_ok
def get_db_config():
    from django.conf import settings
    return dict(
        host=settings.DATABASES["default"]["HOST"],
        engine="mysql",
        name=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        port =settings.DATABASES["default"]["PORT"]
    )
# SQL_DB_CONFIG=dict(
#     host="172.16.7.63",
#     port=3306,
#     user="root",
#     password="123456",
#     name="lv_lms",
#     engine="mysql"
#
# )
# NO_SQL_DB_CONFIG=dict(
#     host="172.16.7.63",
#     port=27017,
#     user="root",
#     password="123456",
#     name="lv_lms"
# )
menu_items=[
    {
        "caption" : "System",
        "items" :[
            {
                "caption":"Accounts",
                "page":"users"
            }
        ]
    },{
        "caption":"Content",
        "items":[
            {
                "caption":"Linguistics",
                "page":"content/linguistics"
            },{
                "caption":"Email",
                "page":"content/email_template"
            }
        ]
    },{
        "caption":"Courseware",
        "items":[
            {
                "caption":"List of Courseware",
                "page":"courseware/list"
            }
        ]
    }
]