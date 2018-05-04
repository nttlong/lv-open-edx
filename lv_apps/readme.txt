Thêm một app bằng các bước sau:
1- Tạo một thư mục app theo mẫu lv_admin
2- Vào file __ini__.py trong thư mục lv_apps đăng ký
quicky.applications.load_app(dict(
    name="<tên app>",
    path= "<Đường dẫn bắt đầu từ thư mục edx-platform>",
    host="lv_admin"
))
