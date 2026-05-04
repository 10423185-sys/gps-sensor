📡 GPS Sensor with CounterFit
📌 Mô tả

Project này mô phỏng GPS sensor bằng CounterFit và đọc dữ liệu NMEA để lấy thông tin vị trí và các dữ liệu GPS khác.

🎯 Chức năng
Kết nối GPS sensor qua CounterFit
Đọc dữ liệu NMEA từ UART
Lấy thông tin:
📍 Latitude / Longitude
⏰ Thời gian (UTC)
📅 Ngày
🚀 Tốc độ
⛰ Độ cao (nếu có)
🧰 Công nghệ sử dụng
Python 3.11
CounterFit
counterfit-connection
counterfit-shims-serial
⚙️ Cách chạy
1. Mở CounterFit
counterfit
2. Cấu hình GPS Sensor
Type: UART GPS
Port: /dev/ttyAMA0
Source: NMEA
3. Chạy chương trình
python app.py
📡 Ví dụ dữ liệu NMEA
$GNRMC,020604.001,A,4738.538654,N,12208.341758,W,0.5,0.0,010203,,,A*68
📊 Kết quả

Chương trình sẽ hiển thị:

Time
Date
Latitude
Longitude
Speed
🎯 Mục tiêu bài học
Hiểu cấu trúc dữ liệu GPS NMEA
Biết cách đọc dữ liệu từ sensor
Xử lý dữ liệu IoT đơn giản bằng Python
🏁 Kết luận

Project mô phỏng hệ thống GPS IoT đơn giản và cách xử lý dữ liệu từ cảm biến thực tế.
