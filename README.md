Môn học: Lưu trữ và xử lý dữ liệu lớn (IT4931)

GVHD: TS. Trần Việt Trung

# Thông tin nhóm
Nhóm: 8

| STT | Họ và Tên           | Mã Sinh Viên | 
|-----|---------------------|--------------|
| 1   | Trần Hàn Minh       | 20210605     | 
| 2   | Hoàng Quốc Việt     | 20210936     | 
| 3   | Trần Văn Lương      | 20215613     | 
| 4   | Lê Đình Thông       | 20215648     | 
| 5   | Nguyễn Nam Hoàng    | 20215382     | 

# Tổng quan về Project: 

Hệ thống phân tích các thông tin về giá taxi tại New York (dựa trên tập dataset Newyork Taxi Trip Data được cung cấp bởi  Ủy ban Taxi và Limousine Thành phố New York). Dự án được thiết kế để xử lý lượng lớn thông tin về các chuyến taxi (giá cả, quãng đường di chuyển, ...) bằng cách sử dụng các framework big data như Kafka, Spark.

# Giới thiệu dataset:
Bộ dữ liệu này là một hồ sơ chi tiết về sự di chuyển đô thị, ghi lại những thông tin chi tiết về mỗi chuyến đi taxi. Từ các điểm dữ liệu thời gian như thời gian đón và thả khách cho đến các khía cạnh không gian liên quan đến vị trí, dữ liệu này cung cấp một cái nhìn chi tiết về các mô hình giao thông đô thị.

Mô tả các cột dữ liệu:

VendorID: Mã nhận dạng của nhà cung cấp TPEP cung cấp bản ghi.

1 = Creative Mobile Technologies, LLC
2 = VeriFone Inc.
tpep_pickup_datetime: Ngày và giờ khi đồng hồ tính tiền được kích hoạt.

tpep_dropoff_datetime: Ngày và giờ khi đồng hồ tính tiền được tắt.

Passenger_count: Số lượng hành khách trên xe, được nhập bởi tài xế.

Trip_distance: Khoảng cách chuyến đi tính bằng dặm, được ghi lại bởi đồng hồ tính tiền.

PULocationID: Mã vùng của Ủy ban Taxi và Limousine (TLC) nơi đồng hồ tính tiền được kích hoạt.

DOLocationID: Mã vùng của TLC nơi đồng hồ tính tiền được tắt.

RateCodeID: Mã giá cước áp dụng vào cuối chuyến đi.

1 = Giá chuẩn
2 = JFK
3 = Newark
4 = Nassau hoặc Westchester
5 = Giá thương lượng
6 = Chuyến đi ghép
Store_and_fwd_flag: Cho biết liệu bản ghi chuyến đi có được lưu trữ trong bộ nhớ của xe trước khi truyền về nhà cung cấp do không có kết nối máy chủ hay không.

Y = Lưu và chuyển tiếp chuyến đi
N = Không lưu và chuyển tiếp chuyến đi
Payment_type: Cách hành khách thanh toán cho chuyến đi, được đại diện bởi một mã số.

1 = Thẻ tín dụng
2 = Tiền mặt
3 = Không tính phí
4 = Tranh chấp
5 = Không rõ
6 = Hủy chuyến đi
Fare_amount: Số tiền vé được tính dựa trên thời gian và khoảng cách.

Extra: Các khoản phí bổ sung, hiện bao gồm phí $0,50 và $1 vào giờ cao điểm và ban đêm.

MTA_tax: Thuế $0,50 tự động được cộng vào dựa trên giá vé đã tính.

Improvement_surcharge: Phí phụ thu $0,30 được cộng vào khi bắt đầu chuyến đi, được áp dụng từ năm 2015.

Tip_amount: Tiền tip qua thẻ tín dụng. (Lưu ý: Tiền tip bằng tiền mặt không được ghi lại ở đây.)

Tolls_amount: Tổng số tiền phí cầu đường phải trả trong chuyến đi.

Total_amount: Tổng số tiền mà hành khách phải trả, không bao gồm tiền tip bằng tiền mặt.

## Mục tiêu của hệ thống:

  - Thiết lập hệ thống ingest dữ liệu theo thời gian thực sử dụng Apache Kafka.
  - Xử lý dữ liệu luồng bằng Apache Spark.
  - Lưu trữ dữ liệu đã xử lý vào cơ sở dữ liệu MySQL.
  - Trực quan hóa dữ liệu đã xử lý bằng Grafana.
  - Điều phối toàn bộ hệ thống bằng Docker.

## Kiến trúc hệ thống:

Các thành phần chính:

  - Kafka Producer: Một script Python lấy dữ liệu các chuyến taxi từ dataset và đưa dữ liệu lên một topic Kafka.
  - Kafka: Nền tảng luồng dữ liệu phân tán, thu thập dữ liệu theo thời gian thực từ Kafka Producer và cung cấp cho việc xử lý.
  - Spark: Hệ thống tính toán phân tán, lấy dữ liệu từ Kafka, xử lý và lưu trữ dữ liệu đã xử lý vào cơ sở dữ liệu MySQL.
  - MySQL: Hệ quản trị cơ sở dữ liệu quan hệ dùng để lưu trữ dữ liệu cổ phiếu đã xử lý.
  - Grafana: Trực quan hóa và giám sát dữ liệu, được sử dụng để tạo các bảng điều khiển và trực quan hóa dữ liệu đã xử lý.

## Yêu cầu

  - Python (phiên bản 3.12)
  - Docker: Cài đặt Docker và Docker Compose trên máy của bạn.
  - Hệ điều hành: Ubuntu 22.04

## Hướng dẫn cài đặt

1. Clone dự án:
   ```
   git clone https://github.com/hawa1222/real-time-data-processing.git
   ```

2. Điều hướng đến thư mục chứa dự án:
   ```
   cd real-time-data-processing
   ```

3. Cài đặt môi trường:

   Chạy file setup_environment.sh để tạo môi trường ảo và cài đặt tất cả các thư viện cần thiết. Thực hiện script này từ thư mục gốc của dự án.
   
   ```
   ./setup_environment.sh
   ```

4. Tạo tệp .env trong thư mục gốc của dự án và cung cấp các biến môi trường theo yêu cầu trong tệp .env_template.

## Hướng dẫn sử dụng

1. Chạy các Docker containers:
   ```
   docker-compose up --build
   ```

   - Lệnh này sẽ xây dựng các image Docker và khởi động các container cho từng dịch vụ (Kafka, Spark, MySQL, và Grafana).

2. Truy cập giao diện Grafana:

  Mở trình duyệt web và truy cập http://localhost:3000. Đăng nhập bằng thông tin bạn đã cung cấp trong tệp .env.

## Các công việc đã làm:

1. Xây dựng hoàn chỉnh toàn bộ hệ thống với Docker

Gồm 6 container:
![image](https://github.com/user-attachments/assets/ab2b31bc-7621-44c0-a0e5-03157b9ac67d)

  - real-time-data-processing-spark-1: Container chạy Apache Spark, dùng để xử lý dữ liệu streaming theo thời gian thực. Spark sẽ xử lý các dữ liệu nhận được từ Kafka hoặc các nguồn khác và thực hiện các tác vụ tính toán.

  - real-time-data-processing-kafka_producer-1: Container Kafka producer, được sử dụng để gửi dữ liệu vào Kafka topic. Dữ liệu này sau đó sẽ được xử lý bởi Spark.

  - real-time-data-processing-grafana-1: Container chạy Grafana. Nó sẽ kết nối với cơ sở dữ liệu MySQL để hiển thị các biểu đồ và số liệu thời gian thực từ dữ liệu đã được xử lý.

  - real-time-data-processing-kafka_broker-1: Container Kafka broker, chịu trách nhiệm nhận và lưu trữ các thông điệp từ các Kafka producer và phân phối chúng tới các Kafka consumer như Spark.

  - real-time-data-processing-zookeeper-1: Container chạy Zookeeper, cung cấp dịch vụ quản lý cluster cho Kafka broker, giữ vai trò đồng bộ và theo dõi trạng thái của các broker trong hệ thống.

  - real-time-data-processing-database-1: Đây là container chạy MySQL, đóng vai trò như cơ sở dữ liệu lưu trữ dữ liệu đã được xử lý và có thể được truy vấn bởi Grafana để hiển thị thông tin.

2. Xây dựng Kafka Producer
Script Python để load dữ liệu lên một topic Kafka. Log có dạng như sau:
![image](https://github.com/user-attachments/assets/b5c65737-ca66-4c9c-bb05-f75affbf4c07)


## TODO:
1. Xây dựng chương trình xử lý dữ liệu từ Kafka với Spark
2. Đưa dữ liệu vào MySQL
3. Cấu hình grafana, xây dựng dashboard để trực quan hóa dữ liệu.

