# CNPM_GameHub
## User Case
1. Guest UsesCase:

2. Player UseCase:
@startuml
left to right direction
skinparam actorStyle hollow

actor Player as "Người chơi"

rectangle "Hệ thống Game" {
    usecase U1 as "Đăng nhập"
    usecase U2 as "Đăng xuất"
    usecase U3 as "Đổi quà"
    usecase U4 as "Chơi game chính thức"
    usecase U5 as "Nhận điểm thưởng"
    usecase U6 as "Xem Bảng xếp hạng"
    usecase U7 as "Viết đánh giá/bình luận"
    usecase U8 as "Xem đánh giá"
    usecase U9 as "Theo dõi điểm tích luỹ"
}

Player -- (U1)
Player -- (U2)
Player -- (U3)
Player -- (U4)
Player -- (U6)
Player -- (U7)
Player -- (U8)
Player -- (U9)

(U4) ..> (U5) : <<include>>
(U3) ..> (U9) : <<include>>
(U7) ..> (U8) : <<extend>>
@enduml


3. ...
...

## Activity
1. User activity
...
2. Player activity
- Đăng nhập
@startuml
title Hoạt động Đăng nhập
start
:Nhập tên người dùng và mật khẩu;
:Nhấn nút "Đăng nhập";
:Gửi thông tin đến hệ thống;
if (Thông tin hợp lệ?) then (có)
  :Xác thực thành công;
  :Truy cập giao diện người dùng;
else (không)
  :Hiển thị thông báo lỗi;
  :Nhập lại thông tin;
  stop
endif
stop
@enduml
- Chơi game và nhận thưởng
@startuml
title Hoạt động Chơi game & Nhận điểm thưởng
start
:Chọn game để chơi;
:Bắt đầu phiên chơi mới;
:Chơi game;
:Kết thúc phiên chơi;
:Hệ thống tính toán điểm số và điểm thưởng;
:Cập nhật điểm thưởng vào tài khoản;
:Hiển thị thông báo nhận điểm thưởng;
stop
@enduml
- Xem BXH và Đánh giá
  @startuml
title Hoạt động Xem BXH & Đánh giá
start
:Chọn một game để xem;
partition "Lựa chọn chức năng" {
  if (Chọn Xem Bảng xếp hạng?) then (có)
    :Hệ thống truy vấn dữ liệu Bảng xếp hạng;
    :Hiển thị danh sách người chơi và điểm số;
  else (không)
    if (Chọn Viết Đánh giá?) then (có)
      :Nhập nội dung đánh giá và điểm số;
      :Gửi đánh giá đến hệ thống;
      :Lưu đánh giá vào cơ sở dữ liệu;
      :Thông báo gửi đánh giá thành công;
    else (không)
      :Hệ thống truy vấn các Review đã có;
      :Hiển thị danh sách các Review;
    endif
  endif
}
stop
@enduml
- Đổi thưởng
  @startuml
title Hoạt động Đổi quà bằng điểm tích luỹ
start
:Truy cập trang đổi quà;
:Chọn món quà muốn đổi;
if (Điểm tích luỹ đủ?) then (có)
  :Trừ điểm khỏi tài khoản;
  :Cập nhật trạng thái đổi quà thành công;
  :Hiển thị thông báo đổi quà thành công;
else (không)
  :Hiển thị thông báo lỗi: "Không đủ điểm";
endif
stop
@enduml
3. ....
...


## Sequence DG:
1. ...
...
2. Player
- Đăng nhập
sequenceDiagram
    participant Player
    participant WebApp
    participant Controller
    participant Service
    participant Infrastructure
    participant Database

    Player->>WebApp: Gửi yêu cầu đăng nhập (username, password)
    WebApp->>Controller: Chuyển tiếp yêu cầu
    Controller->>Service: Gọi hàm authenticate(username, password)
    Service->>Infrastructure: Yêu cầu tìm kiếm người dùng theo username
    Infrastructure->>Database: Truy vấn: `SELECT * FROM users WHERE username = '...'`
    Database-->>Infrastructure: Trả về thông tin người dùng
    Infrastructure-->>Service: Trả về đối tượng `User`
    alt Mật khẩu hợp lệ
        Service->>Infrastructure: Yêu cầu tạo phiên làm việc (session/token)
        Infrastructure-->>Service: Trả về token đã tạo
        Service-->>Controller: Trả về token/thông tin người dùng
        Controller-->>WebApp: Gửi phản hồi thành công (token)
        WebApp-->>Player: Hiển thị giao diện đã đăng nhập
    else Mật khẩu không hợp lệ
        Service-->>Controller: Trả về lỗi xác thực
        Controller-->>WebApp: Gửi phản hồi lỗi
        WebApp-->>Player: Hiển thị thông báo lỗi
    end
- Chơi game nhận điểm
sequenceDiagram
    participant Player
    participant WebApp
    participant Controller
    participant Service
    participant Domain
    participant Infrastructure
    participant Database

    Player->>WebApp: Bắt đầu chơi một game
    WebApp->>Controller: Gọi `startGame(gameId)`
    Controller->>Service: Bắt đầu một phiên chơi mới
    Note over Player,WebApp: Người chơi tương tác và chơi game
    Player->>WebApp: Kết thúc phiên, gửi kết quả (ví dụ: điểm số)
    WebApp->>Controller: Gửi kết quả game (score, gameId)
    Controller->>Service: Xử lý kết quả game
    Service->>Domain: Khởi tạo đối tượng `GameSession` / `Score`
    Service->>Infrastructure: Yêu cầu lưu kết quả
    Infrastructure->>Database: Lưu điểm số và các dữ liệu liên quan
    Database-->>Infrastructure: Ghi nhận thành công
    Infrastructure-->>Service: Xác nhận lưu
    Service->>Service: Tính toán điểm thưởng dựa trên điểm số
    Service->>Infrastructure: Yêu cầu cập nhật điểm thưởng cho người chơi
    Infrastructure->>Database: Cập nhật `points = points + bonus_points` WHERE `userId = '...'`
    Database-->>Infrastructure: Cập nhật thành công
    Infrastructure-->>Service: Trả về điểm mới của người chơi
    Service-->>Controller: Trả về điểm mới và thông tin cập nhật
    Controller-->>WebApp: Gửi phản hồi điểm thưởng
    WebApp-->>Player: Hiển thị điểm số và điểm thưởng nhận được
- Xem BXH và đánh giá
sequenceDiagram
    participant Player
    participant WebApp
    participant Controller
    participant Service
    participant Infrastructure
    participant Database

    Player->>WebApp: Yêu cầu xem Bảng xếp hạng (Leaderboard) game X
    WebApp->>Controller: Gọi `getLeaderboard(gameId)`
    Controller->>Service: Yêu cầu lấy dữ liệu
    Service->>Infrastructure: Yêu cầu truy vấn top scores
    Infrastructure->>Database: Truy vấn bảng xếp hạng game X
    Database-->>Infrastructure: Trả về danh sách người chơi và điểm số
    Infrastructure-->>Service: Trả về danh sách
    Service-->>Controller: Trả về dữ liệu bảng xếp hạng
    Controller-->>WebApp: Gửi dữ liệu để hiển thị
    WebApp-->>Player: Hiển thị bảng xếp hạng

    Player->>WebApp: Yêu cầu xem Đánh giá (Review) game X
    WebApp->>Controller: Gọi `getReviews(gameId)`
    Controller->>Service: Yêu cầu lấy dữ liệu đánh giá
    Service->>Infrastructure: Yêu cầu truy vấn các đánh giá
    Infrastructure->>Database: Truy vấn các đánh giá game X
    Database-->>Infrastructure: Trả về danh sách đánh giá
    Infrastructure-->>Service: Trả về danh sách
    Service-->>Controller: Trả về dữ liệu đánh giá
    Controller-->>WebApp: Gửi dữ liệu để hiển thị
    WebApp-->>Player: Hiển thị các đánh giá và bình luận
- Đổi thưởng
sequenceDiagram
    participant Player
    participant WebApp
    participant Controller
    participant Service
    participant Infrastructure
    participant Database

    Player->>WebApp: Yêu cầu đổi quà (itemId)
    WebApp->>Controller: Gửi request `redeemItem(itemId)`
    Controller->>Service: Yêu cầu xử lý đổi quà
    Service->>Infrastructure: Yêu cầu lấy thông tin quà và điểm của người chơi
    Infrastructure->>Database: Truy vấn điểm của người chơi và giá trị quà tặng
    Database-->>Infrastructure: Trả về điểm hiện tại và giá trị quà
    Infrastructure-->>Service: Trả về dữ liệu
    alt Đủ điểm để đổi
        Service->>Infrastructure: Yêu cầu trừ điểm và ghi nhận quà
        Infrastructure->>Database: Cập nhật `points = points - item_cost` và thêm bản ghi đổi quà
        Database-->>Infrastructure: Cập nhật thành công
        Infrastructure-->>Service: Xác nhận cập nhật
        Service-->>Controller: Trả về thông tin quà tặng đã đổi
        Controller-->>WebApp: Gửi phản hồi thành công
        WebApp-->>Player: Hiển thị thông báo đổi quà thành công
    else Không đủ điểm
        Service-->>Controller: Trả về lỗi không đủ điểm
        Controller-->>WebApp: Gửi phản hồi lỗi
        WebApp-->>Player: Hiển thị thông báo lỗi
    end



3. ...
...




