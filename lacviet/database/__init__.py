import json
from path import Path as path
_nosql_connection = None
_config_ = None

global _config_
if _config_==None:
    # _config_=custom_config()
    PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /edx-platform/lms
    REPO_ROOT = PROJECT_ROOT.dirname()
    with open(PROJECT_ROOT + "/configs.json") as config_file:
        ret_config = json.load(config_file)
        _config_=ret_config
        # _config_.sql.host=ret_config.get("SQL").get("HOST")
            # _config_.sql.port = ret_config.get("SQL").get("PORT")
            # _config_.sql.user = ret_config.get("SQL").get("USER")
            # _config_.sql.password = ret_config.get("SQL").get("PASSWORD")
            # _config_.sql.name = ret_config.get("SQL").get("NAME")
            #
            # _config_.no_sql.host = ret_config.get("NO_SQL").get("HOST")
            # _config_.no_sql.port = int(ret_config.get("NO_SQL").get("PORT"))
            # _config_.no_sql.user = ret_config.get("NO_SQL").get("USER")
            # _config_.no_sql.password = ret_config.get("NO_SQL").get("PASSWORD")
            # _config_.no_sql.name = ret_config.get("SQL").get("NAME")
            # _config_.host_url=ret_config.get("HOST_URL")oh
            # _config_.login_url = ret_config.get("LOGIN_URL")