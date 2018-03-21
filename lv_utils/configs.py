import json
from path import Path as path
import sys
import os
class custom_sql_config:
    "datat base host"
    def __init__(self):
        self.host=""
        self.name=""
        self.port=""
        self.user=""
        self.password=""
class custom_no_sql_config:
    def __init__(self):
        self.host=""
        self.port=27017
        self.name=""
        self.user=""
        self.password=""
class custom_config:
    def __init__(self):
        self.sql=custom_sql_config()
        self.no_sql=custom_no_sql_config()
        self.host_url=""
        self.login_url=""
class features:
    def __init__(self):
        self.AUTH_USE_OPENID_PROVIDER= True
        self.AUTOMATIC_AUTH_FOR_TESTING= True
        self.CUSTOM_COURSES_EDX= True
        self.ENABLE_COMBINED_LOGIN_REGISTRATION= True
        self.ENABLE_CORS_HEADERS= True
        self.ENABLE_COUNTRY_ACCESS=True
        self.ENABLE_CREDIT_API= True
        self.ENABLE_CREDIT_ELIGIBILITY= True
        self.ENABLE_CROSS_DOMAIN_CSRF_COOKIE= True
        self.ENABLE_CSMH_EXTENDED=True
        self.ENABLE_DISCUSSION_HOME_PANEL= True
        self.ENABLE_DISCUSSION_SERVICE= True
        self.ENABLE_EDXNOTES=True
        self.ENABLE_GRADE_DOWNLOADS= True
        self.ENABLE_INSTRUCTOR_ANALYTICS= True
        self.ENABLE_MKTG_SITE=True
        self.ENABLE_MOBILE_REST_API= True
        self.ENABLE_OAUTH2_PROVIDER= True
        self.ENABLE_ONLOAD_BEACON=True
        self.ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES= True
        self.ENABLE_SPECIAL_EXAMS= True
        self.ENABLE_SYSADMIN_DASHBOARD= True
        self.ENABLE_THIRD_PARTY_AUTH= True
        self.ENABLE_VIDEO_BEACON= True
        self.ENABLE_VIDEO_UPLOAD_PIPELINE= True
        self.PREVIEW_LMS_BASE= "preview.localhost:18000"
        self.SHOW_FOOTER_LANGUAGE_SELECTOR= True
        self.SHOW_HEADER_LANGUAGE_SELECTOR= True
_config_=None
def get_config():
    global _config_
    if _config_==None:
        _config_=custom_config()
        PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /edx-platform/lms
        REPO_ROOT = PROJECT_ROOT.dirname()
        with open(PROJECT_ROOT + "/configs.json") as config_file:
            ret_config = json.load(config_file)
            _config_.sql.host=ret_config.get("SQL").get("HOST")
            _config_.sql.port = ret_config.get("SQL").get("PORT")
            _config_.sql.user = ret_config.get("SQL").get("USER")
            _config_.sql.password = ret_config.get("SQL").get("PASSWORD")
            _config_.sql.name = ret_config.get("SQL").get("NAME")

            _config_.no_sql.host = ret_config.get("NO_SQL").get("HOST")
            _config_.no_sql.port = int(ret_config.get("NO_SQL").get("PORT"))
            _config_.no_sql.user = ret_config.get("NO_SQL").get("USER")
            _config_.no_sql.password = ret_config.get("NO_SQL").get("PASSWORD")
            _config_.no_sql.name = ret_config.get("SQL").get("NAME")
            _config_.host_url=ret_config.get("HOST_URL")
            _config_.login_url = ret_config.get("LOGIN_URL")
    return  _config_
def get_host_url():
    return  get_config().host_url
def get_login_url():
    return get_config().login_url
def lms_load_configs(AUTH_TOKENS):

    _c_config=AUTH_TOKENS.get("DATABASES").get("default")
    _c_config.update({"HOST": get_config().sql.host});
    _c_config.update({"NAME": get_config().sql.name});
    _c_config.update({"PORT": get_config().sql.port});
    _c_config.update({"USER": get_config().sql.user});
    _c_config.update({"PASSWORD": get_config().sql.password});

    _c_config = AUTH_TOKENS.get("DATABASES").get("student_module_history")
    _c_config.update({"HOST": get_config().sql.host});
    _c_config.update({"NAME": get_config().sql.name});
    _c_config.update({"PORT": get_config().sql.port});
    _c_config.update({"USER": get_config().sql.user});
    _c_config.update({"PASSWORD": get_config().sql.password});

    lms_load_features(AUTH_TOKENS)
    return  AUTH_TOKENS
def cms_load_configs(AUTH_TOKENS):
    mongo_host = get_config().no_sql.host
    mongo_user = get_config().no_sql.user
    mongo_password = get_config().no_sql.password
    mongo_port = get_config().no_sql.port
    mongo_db_name = get_config().no_sql.name
    sql_host=get_config().sql.host
    sql_port = get_config().sql.port
    sql_password = get_config().sql.password
    sql_user = get_config().sql.user
    sql_name= get_config().sql.name


    _config_ = AUTH_TOKENS.get("CONTENTSTORE").get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    _config_ = AUTH_TOKENS.get("CONTENTSTORE").get("OPTIONS")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    _config_ = AUTH_TOKENS.get("DATABASES").get("default")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    _config_ = AUTH_TOKENS.get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    ########

    _config_ = AUTH_TOKENS.get("MODULESTORE").get("default").get("OPTIONS").get("stores")[0].get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    _config_ = AUTH_TOKENS.get("MODULESTORE").get("default").get("OPTIONS").get("stores")[1].get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    _config_ = AUTH_TOKENS.get("CONTENTSTORE").get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    _config_ = AUTH_TOKENS.get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})

    #---------------my-sql-----------------
    _config_=AUTH_TOKENS.get("DATABASES").get("default")
    _config_.update({"HOST":sql_host})
    _config_.update({"NAME": sql_name})
    _config_.update({"PASSWORD": sql_password})
    _config_.update({"PORT": sql_port})
    _config_.update({"USER": sql_user})

    _config_ = AUTH_TOKENS.get("DATABASES").get("read_replica")
    _config_.update({"HOST": sql_host})
    _config_.update({"NAME": sql_name + "_csmh"})
    _config_.update({"PASSWORD": sql_password})
    _config_.update({"PORT": sql_port})
    _config_.update({"USER": sql_user})

    _config_=AUTH_TOKENS.get("DATABASES").get("student_module_history")
    _config_.update({"HOST": sql_host})
    _config_.update({"NAME": sql_name+"_csmh"})
    _config_.update({"PASSWORD": sql_password})
    _config_.update({"PORT": sql_port})
    _config_.update({"USER": sql_user})

    return AUTH_TOKENS
def lms_load_features(AUTH_TOKENS):
    _f_=AUTH_TOKENS.get("FEATURES")
    fx=features()
    for key, value in _f_.iteritems():
        _f_.update({key:getattr(fx,key)})
