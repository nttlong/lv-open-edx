Moi package nam trong thu muc "lv-packages";



De python dinh vi duoc cac package trong thu muc "lv-packages" lam cac buoc sau:
    1- vao file lsm/evn/common.py tim dong sys.path.append(REPO_ROOT)
    chen them dong sys.path.append(REPO_ROOT+"/lv-packages")

 * Tich hop phan Login:
    1- Vao trang  lms/url.py:
        - Them "from Login_lv import *"
        - urlpatterns them "url(r'^signin/(?P<username>[\w\-]+)/$', 'Login_lv.views.signin', name="signin"),"
CAU HINH DATABASE:
    1- Trong file lms.auth.json them :
            "MYSQL_CONFIG":{
            "HOST":"<Dia chi IP>",
            "PORT":"3306",
             "NAME":"<Database name>",
            "USER":"<user>",
            "PASSWORD":"<password>"},
            "HOST_URL":"http://0.0.0.0:8000"
    2- Trong file lsm/envs/aws.py tim den dong
        "with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
            AUTH_TOKENS = json.load(auth_file)"

            them cac dong
            AUTH_TOKENS.get("DATABASES").get("default").update({"HOST":AUTH_TOKENS.get("MYSQL_CONFIG").get("HOST")});
            AUTH_TOKENS.get("DATABASES").get("default").update({"NAME": AUTH_TOKENS.get("MYSQL_CONFIG").get("NAME")});
            AUTH_TOKENS.get("DATABASES").get("default").update({"PORT": AUTH_TOKENS.get("MYSQL_CONFIG").get("PORT")});
            AUTH_TOKENS.get("DATABASES").get("default").update({"USER": AUTH_TOKENS.get("MYSQL_CONFIG").get("USER")});
            AUTH_TOKENS.get("DATABASES").get("default").update({"PASSWORD":AUTH_TOKENS.get("MYSQL_CONFIG").get("PASSWORD")});

            AUTH_TOKENS.get("DATABASES").get("student_module_history").update({"HOST":AUTH_TOKENS.get("MYSQL_CONFIG").get("HOST")});
            AUTH_TOKENS.get("DATABASES").get("student_module_history").update({"NAME": AUTH_TOKENS.get("MYSQL_CONFIG").get("NAME")});
            AUTH_TOKENS.get("DATABASES").get("student_module_history").update({"PORT": AUTH_TOKENS.get("MYSQL_CONFIG").get("PORT")});
            AUTH_TOKENS.get("DATABASES").get("student_module_history").update({"USER": AUTH_TOKENS.get("MYSQL_CONFIG").get("USER")});
            AUTH_TOKENS.get("DATABASES").get("student_module_history").update({"PASSWORD": AUTH_TOKENS.get("MYSQL_CONFIG").get("PASSWORD")});
             /**Luu y: danh phim tab cung dong */
    3- Trong file cms.auth.json them duoi cung cac dong sau;
           "MYSQL_CONFIG":{
        "HOST":"172.16.11.217",
        "PORT":"3306",
        "NAME":"bitnami_edxapp",
        "USER":"root",
        "PASSWORD":"123456"
        },
        "MONGODB_CONFIG":{
            "HOST":"172.16.11.217",
            "PORT":"27018",
            "NAME":"bitnami_edxapp",
            "USER":"",
            "PASSWORD":""
        }
    4- Trong file cms/evns/aws.py tim
            with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
            AUTH_TOKENS = json.load(auth_file)
            Them o duoi cac dong sau:
            # begin-------------------------------
            mongo_host = AUTH_TOKENS.get("MONGODB_CONFIG").get("HOST")
            mongo_user = AUTH_TOKENS.get("MONGODB_CONFIG").get("USER")
            mongo_password = AUTH_TOKENS.get("MONGODB_CONFIG").get("PASSWORD")
            mongo_port = AUTH_TOKENS.get("MONGODB_CONFIG").get("PORT")
            mongo_db_name = AUTH_TOKENS.get("MONGODB_CONFIG").get("NAME")


            _config_=AUTH_TOKENS.get("CONTENTSTORE").get("DOC_STORE_CONFIG")
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

            _config_ = AUTH_TOKENAMENS.get("DOC_STORE_CONFIG")
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

            /**Luu y: danh phim tab cung dong */

CAU HINH SERVICE:
     1- Vao file lms/url.py them
        |---------------------------------------------------------------------------|
        | url(r'^web_services/$', 'lv_ws.views.web_services', name="web_services"), |
        |___________________________________________________________________________|