Moi package nam trong thu muc "lv-packages";



De python dinh vi duoc cac package trong thu muc "lv-packages" lam cac buoc sau:
    1- vao file lsm/evn/common.py tim dong sys.path.append(REPO_ROOT)
    chen them dong sys.path.append(REPO_ROOT+"/lv-packages")

 * Tich hop phan Login:
    1- Vao trang  lms/url.py:
        - Them "from Login_lv import *"
        - urlpatterns them "url(r'^signin/(?P<username>[\w\-]+)/$', 'Login_lv.views.signin', name="signin"),"
CAU HINH DATABASE:
    1- Mo file configs.json trong thu muc "lv-packages" sua cau hinh :
          {
          "SQL":{
            "HOST":"zzzz",
            "NAME":"bitnami_edxapp",
            "USER":"root",
            "PASSWORD":"123456",
            "PORT":"3306"
          },
          "NO_SQL":{
            "HOST":"zzzz",
            "NAME":"bitnami_edxapp",
            "USER":"root",
            "PASSWORD":"123456",
            "PORT":"27018"
          },
          "HOST_URL":"http://0.0.0.0:8000"
        }
    2- Trong file lsm/envs/aws.py tim den dong
        "with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
            AUTH_TOKENS = json.load(auth_file)"

            them cac dong
                from lv_utils import  configs
                configs.lms_load_configs(AUTH_TOKENS)

             /**Luu y: danh phim tab cung dong */
        tim de dong ENV_TOKENS = json.load(env_file)
            from lv_utils import configs
            configs.lms_load_envs(ENV_TOKENS)
    4- Trong file cms/evns/aws.py tim
            with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
            AUTH_TOKENS = json.load(auth_file)
            from lv_utils import  configs
                configs.cms_load_configs(AUTH_TOKENS)

CAU HINH SERVICE:
     1- Vao file lms/url.py them
        |---------------------------------------------------------------------------|
        | url(r'^web_services/$', 'lv_ws.views.web_services', name="web_services"), |
        |___________________________________________________________________________|
