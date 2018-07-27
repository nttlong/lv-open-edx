

EMAIL
______________________________________


Cài đặt email vào file site.json trong thư mục lv-packages
===========================================================


Thêm các mục sau:


 "BUGS_EMAIL": "requesthcs@lacviet.com.vn",

 "BULK_EMAIL_DEFAULT_FROM_EMAIL": "requesthcs@lacviet.com.vn",


  "CONTACT_EMAIL": "requesthcs@lacviet.com.vn",

  "DEFAULT_FEEDBACK_EMAIL": "requesthcs@lacviet.com.vn",

  "DEFAULT_FROM_EMAIL": "registration@example.com",

  "SERVER_EMAIL": "devops@example.com",

  "EMAIL_HOST": "webmail.lacviet.com.vn",

  "TECH_SUPPORT_EMAIL": "technical@example.com",

  "UNIVERSITY_EMAIL": "university@example.com",

  "EMAIL_PORT": 25,

  "EMAIL_USE_TLS": false,

  "EMAIL_HOST_PASSWORD":...

  "EMAIL_HOST_USER":...


Các template email nằm hết trong thư mục:
==============================================


    **lms/templates/emails**


Các tham số khác:
---------------------

Cho phép giản viên liên lạc với học viên trong lms

Thêm field này vào file lms.env.js
on hoặc file features.json trong thư mục lv-packages

"ENABLE_INSTRUCTOR_EMAIL":true

Cho phép xác nhận email trước khi tham gia khóa học:

"REQUIRE_COURSE_EMAIL_AUTH": true

