# 🏥 Smart Connected Platform (SCP) - Hub

Nền tảng kết nối thông minh (SCP) là trung tâm điều hành tích hợp cho các hệ sinh thái Y tế, Vận hành hạ tầng, Khoa học giáo dục và AI.

## 📁 Cấu trúc Repository (Scientific Hub Structure)

```
Hospital_Management (SCP Repo)
├── index.html              # Hub Trung tâm - Landing Page chính
├── hub_assets/             # Tài nguyên dùng riêng cho Hub (Hình ảnh, Icons)
│   └── audit_preview.jpg   # Preview cho hệ thống 83 Tiêu chí
├── README.md               # Hướng dẫn này
├── CHANGELOG.md            # Nhật ký cập nhật
└── Archive/                # Lưu trữ mã nguồn cũ (Legacy Code)
    └── Legacy_Core/        # Toàn bộ hệ thống cũ trước khi tách Repo
```

## 🚀 Hệ sinh thái liên kết (Micro-services Architecture)

Thay vì một Repository khổng lồ, SCP được tách thành các hệ thống chuyên biệt để tối ưu tốc độ và quản lý:

1. **[HMIS - Quản lý Bệnh Viện](https://9dpi.github.io/hmis/)**
   - Dashboard điều hành y tế, quản lý bệnh nhân và cơ sở vật chất.
2. **[BMIS - Quản lý Tòa Nhà](https://9dpi.github.io/bmis/)**
   - Giám sát hạ tầng, điện nước, an ninh và dịch vụ cư dân.
3. **[83 Tiêu Chí Chất Lượng](https://9dpi.github.io/83_TC_BenhVien/)**
   - Công cụ đánh giá tiêu chuẩn chất lượng Bệnh viện.
4. **[Science & Education Lab]**
   - Quantum Dharma, Cosmic Life, Silk Destiny.

## 🛠️ Công nghệ sử dụng

- **Frontend**: Vanilla HTML5, CSS3 (Modern Glassmorphism Design).
- **Icons**: Font Awesome 6.
- **AI Integration**: Google Apps Script (GAS) Chatbot.
- **Micro-frontend**: Redirect-based routing.

## 🔧 Bảo trì Hub

- Để chỉnh sửa giao diện Hub, chỉnh sửa trực tiếp `index.html`.
- Các asset mới cho Hub nên được đặt vào folder `hub_assets`.
- Khi có Module mới, cập nhật danh sách `app-grid` trong `index.html`.

---
**Version**: 3.0 (Scientific Reorganization)  
**Last Updated**: 2026-01-07  
**Maintained by**: 9dpi Development Team
