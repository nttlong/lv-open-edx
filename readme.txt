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

