import quicky
import os
quicky.authorize.set_config(
    host="172.16.7.63",
    port=27017,
    user="root",
    password="123456",
    name="lv_lms"

)
quicky.language.set_config(
    host="172.16.7.63",
    port=27017,
    user="root",
    password="123456",
    name="lv_lms",
    collection="sys_language"
)
lv_admin=quicky.applications.load_app(dict(
    name="lv-admin",
    path= "lv-packages/apps/lv_admin",
    host="lv_admin"
))
lv_cms=quicky.applications.load_app(dict(
    name="lv-cms",
    path= "lv-packages/apps/lv_cms",
    host="lv_cms"
))
