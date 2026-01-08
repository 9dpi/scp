# 🏥 Smart Connected Platform (SCP) - Hub

Nền tảng kết nối thông minh (SCP) là trung tâm điều hành tích hợp cho các hệ sinh thái Y tế, Vận hành hạ tầng, Khoa học giáo dục và AI.

## 🌐 Landing Page chính thức
**[https://9dpi.github.io/scp/](https://9dpi.github.io/scp/)**

## 📁 Cấu trúc Repository (Scientific Hub Structure)

```
Hospital_Management (SCP Repo)
├── index.html              # Landing Page cổng điều hướng (SCP Hub)
├── hub_assets/             # Tài nguyên dùng riêng cho Hub (Hình ảnh, Icons)
├── README.md               # Hướng dẫn này
├── CHANGELOG.md            # Nhật ký cập nhật
└── Archive/                # Lưu trữ mã nguồn & Tài nguyên hệ thống
```

## 🚀 Hệ sinh thái liên kết (Micro-services Architecture)

Thay vì một Repository khổng lồ, SCP được tách thành các hệ thống chuyên biệt để tối ưu tốc độ và quản lý:

1. **[HMIS - Quản lý Bệnh Viện](https://9dpi.github.io/hmis/)**
   - Dashboard điều hành y tế, quản lý bệnh nhân và cơ sở vật chất.
2. **[BMIS - Quản lý Tòa Nhà](https://9dpi.github.io/bmis/)**
   - Giám sát hạ tầng, điện nước, an ninh và dịch vụ cư dân.
3. **[83 Tiêu Chí Chất Lượng](https://9dpi.github.io/83_TC_BenhVien/)**
   - Công cụ đánh giá tiêu chuẩn chất lượng Bệnh viện.

## 🔮 Tầm nhìn Công nghệ 2026 (Roadmap)

### 1. Bệnh viện không dây (Wireless Hospitals)
- **Thiết bị Y tế Module hóa**: Mỗi máy đo sinh tồn, bơm tiêm điện là một module IoT độc lập.
- **Kết nối Plug-and-Play**: Thiết bị tự động nhận diện phòng bệnh và đẩy dữ liệu về hồ sơ bệnh nhân (EMR) theo thời gian thực.
- **Giao thức Bảo mật mới**: Zero-trust architecture cho thiết bị y tế biên (Edge Devices).

### 2. Bằng chứng số & Thị giác máy tính (AI Computer Vision)
- **Giám sát vệ sinh tự động**: Camera thông minh (Smart AI Cam) tự động nhận diện khu vực đã được làm sạch.
- **Xác thực không chạm**: Loại bỏ quy trình báo cáo thủ công; AI tự động tick "Hoàn thành" khi phát hiện quy trình vệ sinh đạt chuẩn.
- **Tương thích ngược**: Hệ thống hiện tại (Ảnh chụp báo cáo) là bước đệm (V1) cho luồng dữ liệu AI tự động (V2).

## 🛠️ Công nghệ sử dụng

- **Frontend**: Vanilla HTML5, CSS3 (Modern Glassmorphism Design).
- **Icons**: Font Awesome 6.
- **AI Integration**: Google Apps Script (GAS) Chatbot.
- **Database Backend**: Google Sheets & Apps Script (Lean Implementation).

---
**Version**: 3.1 (Official URL Launch)  
**Last Updated**: 2026-01-07  
**Maintained by**: 9dpi Development Team
