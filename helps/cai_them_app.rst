=============================================
Để cài đặt  thêm 1 app làm theo các bước sau:
=============================================

1. Vào file lv_apps/__init__.py khai báo thêm 1 app:

    Ví dụ:

        lv_admin=quicky.applications.load_app(dict(

            name="lv-admin", # tên của app nên đặt cố định

            path= "lv-packages/apps/lv_admin", # đường dẫn tương đối đến thư mục của app

            host="lv_admin" # host sub directory

        ))

    **Lưu ý**: **Trong file 'apps/edx/edx-platform/lms/envs/common.py' phải setup các dòng sau**:

        sys.path.append(REPO_ROOT)

        sys.path.append(REPO_ROOT+"/lv-packages")

        sys.path.append(PROJECT_ROOT / 'djangoapps')

        sys.path.append(COMMON_ROOT / 'djangoapps')

        import lv_apps

  2. Vào file 'apps/edx/edx-platform/lms/urls.py', thêm :

    from quicky import applications

    app=applications.get_app_by_name("<app name>")

        Ví dụ:

            from quicky import applications

            lv_admin_app=applications.get_app_by_name("lv-admin")

3. Thêm url của App vào phần url của lms hoặc cms:

        Bằng cách gọi hàm: url của app, ví dụ:

            urlpatterns = (

                '',

                lv_admin_app.urls,