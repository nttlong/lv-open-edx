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
_features=None
_cms_features=None
_site_configs=None
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
    _c_config.update({"HOST": get_config().sql.host})
    _c_config.update({"NAME": get_config().sql.name})
    _c_config.update({"PORT": get_config().sql.port})
    _c_config.update({"USER": get_config().sql.user})
    _c_config.update({"PASSWORD": get_config().sql.password})

    _c_config = AUTH_TOKENS.get("DATABASES").get("student_module_history")
    _c_config.update({"HOST": get_config().sql.host})
    _c_config.update({"NAME": get_config().sql.name})
    _c_config.update({"PORT": get_config().sql.port})
    _c_config.update({"USER": get_config().sql.user})
    _c_config.update({"PASSWORD": get_config().sql.password})


    _c_config = AUTH_TOKENS.get("CONTENTSTORE").get("DOC_STORE_CONFIG")
    _c_config.update({"db":get_config().no_sql.name})
    _c_config.update({"host": get_config().no_sql.host})
    _c_config.update({"password": get_config().no_sql.password})
    _c_config.update({"port": get_config().no_sql.port})
    _c_config.update({"user": get_config().no_sql.user})

    _c_config = AUTH_TOKENS.get("CONTENTSTORE").get("OPTIONS")
    _c_config.update({"db": get_config().no_sql.name})
    _c_config.update({"host": get_config().no_sql.host})
    _c_config.update({"password": get_config().no_sql.password})
    _c_config.update({"port": get_config().no_sql.port})
    _c_config.update({"user": get_config().no_sql.user})

    _c_config = AUTH_TOKENS.get("DOC_STORE_CONFIG")
    _c_config.update({"db": get_config().no_sql.name})
    _c_config.update({"host": get_config().no_sql.host})
    _c_config.update({"password": get_config().no_sql.password})
    _c_config.update({"port": get_config().no_sql.port})
    _c_config.update({"user": get_config().no_sql.user})

    _config_=AUTH_TOKENS.get("MODULESTORE").get("default").get("OPTIONS").get("stores")[0].get("DOC_STORE_CONFIG")
    _c_config.update({"db": get_config().no_sql.name})
    _c_config.update({"host": get_config().no_sql.host})
    _c_config.update({"password": get_config().no_sql.password})
    _c_config.update({"port": get_config().no_sql.port})
    _c_config.update({"user": get_config().no_sql.user})

    _config_ = AUTH_TOKENS.get("MODULESTORE").get("default").get("OPTIONS").get("stores")[1].get("DOC_STORE_CONFIG")
    _c_config.update({"db": get_config().no_sql.name})
    _c_config.update({"host": get_config().no_sql.host})
    _c_config.update({"password": get_config().no_sql.password})
    _c_config.update({"port": get_config().no_sql.port})
    _c_config.update({"user": get_config().no_sql.user})



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
    _config_.update({"db": mongo_db_name})


    _config_ = AUTH_TOKENS.get("CONTENTSTORE").get("OPTIONS")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

    _config_ = AUTH_TOKENS.get("DATABASES").get("default")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

    _config_ = AUTH_TOKENS.get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

    ########

    _config_ = AUTH_TOKENS.get("MODULESTORE").get("default").get("OPTIONS").get("stores")[0].get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

    _config_ = AUTH_TOKENS.get("MODULESTORE").get("default").get("OPTIONS").get("stores")[1].get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

    _config_ = AUTH_TOKENS.get("CONTENTSTORE").get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

    _config_ = AUTH_TOKENS.get("DOC_STORE_CONFIG")
    _config_.update({"host": mongo_host})
    _config_.update({"user": mongo_user})
    _config_.update({"password": mongo_password})
    _config_.update({"port": mongo_port})
    _config_.update({"db": mongo_db_name})

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
def lms_load_envs(EVNS):
    PROJECT_ROOT = path(__file__).abspath().dirname().dirname()

    if _features==None:
        with open(PROJECT_ROOT + "/features.json") as config_file:
            ret_config = json.load(config_file)
    for key in ret_config.keys():
        EVNS.get("FEATURES").update({key:ret_config.get(key)})
    if _site_configs==None:
        with open(PROJECT_ROOT + "/site.json") as site_config_file:
            ret_config = json.load(site_config_file)

    for key in ret_config.keys():
        if key=="COMPREHENSIVE_THEME_DIRS" or key=="COMPREHENSIVE_THEME_LOCALE_PATHS":
            thems=[]
            for skey in ret_config.get(key).keys():
                thems.append(str(PROJECT_ROOT+"/"+ ret_config.get(key).get(skey).get("name")))
            EVNS.update({key:thems})
        else:
            if(key=="COMPREHENSIVE_THEME_DIR" or key=="STATIC_ROOT_BASE"):
                EVNS.update({key: str(PROJECT_ROOT+"/"+ ret_config.get(key))})
            else:
                if(key=="DEFAULT_SITE_THEME"):
                    EVNS.update({key: str(ret_config.get(key))})
                else:
                    EVNS.update({key:ret_config.get(key)})
    return
def cms_load_envs(EVNS):
    PROJECT_ROOT = path(__file__).abspath().dirname().dirname()

    if _cms_features == None:
        with open(PROJECT_ROOT + "/features_cms.json") as config_file:
            ret_config = json.load(config_file)
    for key in ret_config.keys():
        EVNS.get("FEATURES").update({key: ret_config.get(key)})
    if _site_configs == None:
        with open(PROJECT_ROOT + "/site_cms.json") as site_config_file:
            ret_config = json.load(site_config_file)
    for key in ret_config.keys():
        if key == "COMPREHENSIVE_THEME_DIRS" or key == "COMPREHENSIVE_THEME_LOCALE_PATHS":
            thems = []
            for skey in ret_config.get(key).keys():
                thems.append(str(PROJECT_ROOT + "/themes/" + ret_config.get(key).get(skey).get("name")))
            EVNS.update({key: thems})
        else:
            if (key == "COMPREHENSIVE_THEME_DIR" or key=="STATIC_ROOT_BASE"):
                EVNS.update({key: str(PROJECT_ROOT + "/themes/" + ret_config.get(key))})
            else:
                if (key == "DEFAULT_SITE_THEME" ):
                    EVNS.update({key: str(PROJECT_ROOT + "/themes/" + ret_config.get(key))})
                else:
                    EVNS.update({key: ret_config.get(key)})
    return
def lms_load_db_config_of_module_store(settings):
    # _c_config={}
    # _c_config.update({"db": get_config().no_sql.name})
    # _c_config.update({"host": get_config().no_sql.host})
    # _c_config.update({"password": get_config().no_sql.password})
    # _c_config.update({"port": get_config().no_sql.port})
    # _c_config.update({"user": get_config().no_sql.user})
    #
    # settings.MODULESTORE['default'].update({'DOC_STORE_CONFIG':_c_config})
    # settings.MODULESTORE['default'].update({'OPTIONS': _c_config})
    # settings.CONTENTSTORE.update({'DOC_STORE_CONFIG':_c_config})
    # settings.CONTENTSTORE['ADDITIONAL_OPTIONS'].update({'default': _c_config})


    return
def apply_no_sql_db_config(options):
    if(options==None):
        options={}

    options.update({"db": get_config().no_sql.name})
    options.update({"host": get_config().no_sql.host})
    options.update({"password": get_config().no_sql.password})
    options.update({"port": get_config().no_sql.port})
    options.update({"user": get_config().no_sql.user})
    return  options

