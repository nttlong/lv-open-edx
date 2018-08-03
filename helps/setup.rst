Moi package nam trong thu muc "lv-packages";



De python dinh vi duoc cac package trong thu muc "lv-packages" lam cac buoc sau:
    1- vao file lsm/evn/common.py tim dong sys.path.append(REPO_ROOT)
    chen them cac dong sau:


        sys.path.append(REPO_ROOT + "/lv-packages")

        sys.path.append(REPO_ROOT + "/lv-packages/apps")

        sys.path.append(PROJECT_ROOT / 'djangoapps')

        sys.path.append(COMMON_ROOT / 'djangoapps')

        import lv_apps

 * Tich hop phan Login (tuy chon):
    1- Vao trang  lms/url.py:

        - Them "from Login_lv import \*"

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

                **Luu y: danh phim tab cung dong**

                tim den dong ENV_TOKENS = json.load(env_file) them cac dong sau

                    from lv_utils import configs

                    configs.lms_load_envs(ENV_TOKENS)

    4- Trong file cms/evns/aws.py tim

            with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:

                AUTH_TOKENS = json.load(auth_file)

                from lv_utils import  configs

                    configs.cms_load_configs(AUTH_TOKENS)

            Tim den dong ENV_TOKENS = json.load(env_file) them cac dong sau:

                from lv_utils import  configs

                configs.cms_load_envs(ENV_TOKENS)

    5- Cau hinh X module:

            Trong file "edx_platform/common/lib/xmodule/xmodule/modulestore/django.py"

            Tim den dong 'return disabled_xblock_types' Them:

            from lv_utils import configs

            configs.apply_no_sql_db_config(doc_store_config)

CAU HINH SERVICE:

     1- Vao file cms/url.py them

        url(r'^web_services/$', 'lv_ws.views.web_services', name="web_services"),


FIX LOI SEARCH:

    vao file lms/urls.py thay:

    #url(r'^search/', include('search.urls')),

    url(r'^search/', include('searchdata_lv.urls'), name='course_discovery')


Các file quan trọng cần phải xem là:

1- lv_apps/readme.txt (cách thêm một app)

2- themes/readme.txt (Các cài đặt theme cho production)


