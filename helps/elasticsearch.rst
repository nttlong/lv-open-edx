For Windows server
===========================
Vào thư mục: "C:\ProgramData\Elastic\Elasticsearch\config" mở file: elasticsearch.yml

    Thêm 2 dòng sau (cho phép remote access trên windows):

        action.auto_create_index: false

        network.host: 0.0.0.0