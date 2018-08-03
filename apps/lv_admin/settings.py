# -*- coding: utf-8 -*-
name="lv_admin"
is_public=True
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
        "caption" : "Phân quyền",
        "items" :[
            {
                "caption":"Quản lý tài khoản",
                "page":"users"
            }
        ]
    }
]