For Windows server
===========================
Vào thư mục: "C:\ProgramData\Elastic\Elasticsearch\config" mở file: elasticsearch.yml

    Thêm 2 dòng sau (cho phép remote access trên windows):

        action.auto_create_index: false

        network.host: 0.0.0.0


Cài đặt đúng version elasticsearch
=========================================

Với centos hoặc redhat

    1.Thư mục lưu trữ dữ liệu nằm trong:

        /var/lib/elasticseedhatarch/

    2. File cấu hình nằm trong:

        /etc/elasticsearch/elasticsearch.yml

Mỗi một node của elasticsearch sẽ có 1 tên phân biệt, dựa vào tên này mà ES sẽ tạo thư mục lưu trữ có cùng tên

Lện sau đây sẽ cho phép ES đọc và gi dữ liệu lên thư mục /var/lib/elasticsearch/

    sudo chown -R elasticsearch:elasticsearch /var/lib/elasticsearch/

Kiểm tra ES status:

    sudo service elasticsearch status

Restart ES:

    sudo service elasticsearch restart

Kiểm tra version:

    curl -XGET 'localhost:9200' or use web browser with localhost:9200

Shutdown tất cả các node trên cùng 1 server:

    sudo systemctl stop elasticsearch.service

Start tất cả các node trên cùng 1 server:

    sudo systemctl start elasticsearch.service

Lưu ý: Sau khi cấu hình ES thì phải restart lại server bằng lệnh: shutdown -r now


Nạp lại tất cả các service:


    sudo /bin/systemctl daemon-reload
    sudo /bin/systemctl enable elasticsearch.service
    sudo /bin/systemctl start elasticsearch.service

Gỡ bỏ:

    sudo yum remove elasticsearch

Cài đặt đúng version cho open edx:

    sudo yum localinstall elasticsearch-1.5.2.noarch.rpm

Kiểm tra tình trạng:

    http://localhost:9200/_cluster/health

Trong một số trường hợp có thể dùng kill SIGNAL PID để stop service.



Các file source code liên quan đến phần search:
====================================================

    1.apps/edx/edx-platform/cms/djangoapps/contentstore/views/course.py hàm "course_search_index_handler" thực thi mỗi khi vào trong cms đánh index.

        cms/djangoapps/contentstore/courseware_index.py -> do_course_reindex


Quan trong:

    Disable thu muc:

    1. apps/edx/venvs/edxapp/lib/python2.7/site-packages/elasticsearch

    2. apps/edx/venvs/edxapp/lib/python2.7/site-packages/urllib3



Cài phiên bản chạy trên Redhat
==================================

    1. Gỡ bỏ:

        sudo yum remove elasticsearch

    2. Cài java:

        sudo yum install java-1.8.0-openjdk.x86_64

    3. Download Elasticsearch:

        wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.3.noarch.rpm

    4. Cài đặt:

        sudo rpm -ivh elasticsearch-1.7.3.noarch.rpm

    5. Tạo file elasticsearch.yaml trong thư mục /etc/elasticsearch/elasticsearch.yml

        Nội dung như sau:

            cluster.name: lv_elasticsearch_2018 #tên

            node.name: "lacviet2018"

            node.master: true

            node.data: true




    6. Vào file apps/edx/edx-platform/lv-packages/site_cms.json và file apps/edx/edx-platform/lv-packages/site.json

            Thêm các dòng sau:

                "ELASTIC_SEARCH_CONFIG": [

                    {

                        "host": "172.16.7.63",

                        "port": 9200,

                        "use_ssl": false

                    }

                ]

    7. Vào file apps/edx/edx-platform/lv-packages/features.json kiểm tra:


        "ENABLE_COURSEWARE_INDEX": true

    8. Vào file apps/edx/edx-platform/lv-packages/features_cms.json kiểm tra:


        "ENABLE_COURSEWARE_INDEX":true,

        "ENABLE_LIBRARY_INDEX":true,