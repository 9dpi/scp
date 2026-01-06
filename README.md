# 🏥 SCP HMIS - Hospital Management Information System

## 📁 Cấu trúc Dự án

```
Hospital_Management/
├── index.html                          # Trang chính của hệ thống
├── show-app.html                       # Demo ứng dụng mobile
│
├── assets/                             # Tài nguyên tĩnh
│   ├── css/                           # Stylesheets
│   │   ├── main.css                   # CSS chính - Layout, base styles
│   │   ├── components.css             # CSS cho components (sidebar, cards, etc.)
│   │   └── pages/                     # CSS riêng cho từng trang (future use)
│   │
│   ├── js/                            # JavaScript modules
│   │   ├── app.js                     # Script chính - khởi tạo ứng dụng
│   │   ├── charts.js                  # Xử lý biểu đồ Chart.js
│   │   ├── data-service.js            # Tích hợp Google Sheets API
│   │   └── components/                # JS components (future use)
│   │
│   └── images/                        # Hình ảnh
│       ├── 3d.png                     # Mô hình kiến trúc 3D
│       ├── 3d-electric.png            # Mô hình hệ thống điện
│       ├── 3d-water.png               # Mô hình hệ thống nước
│       └── 3d-fire.png                # Mô hình hệ thống PCCC
│
├── pages/                             # Các trang phụ
│   ├── anninh_baove.html              # Quản lý An ninh Bảo vệ
│   ├── bacsy.html                     # Quản lý Bác sỹ
│   ├── benh_nhan.html                 # Quản lý Bệnh nhân
│   ├── bep.html                       # Quản lý Bếp
│   ├── dieuduong.html                 # Quản lý Điều dưỡng
│   ├── house_keeping.html             # Quản lý Vệ sinh
│   ├── kehoach_tonghop.html           # Kế hoạch Tổng hợp
│   ├── kho.html                       # Quản lý Kho
│   ├── laixe_capcuu.html              # Quản lý Lái xe Cấp cứu
│   ├── nhanvien_kythat_thietbi.html   # Quản lý Kỹ thuật Thiết bị
│   ├── quanly.html                    # Quản lý
│   └── quanly_chatluong.html          # Quản lý Chất lượng
│
├── shared/                            # Shared components (future use)
│   ├── header.html                    # Header component
│   ├── sidebar.html                   # Sidebar component
│   └── footer.html                    # Footer component
│
├── Archive/                           # Tài liệu dự án
│   ├── Infographic.png
│   ├── PROJECT CHARTER - HMIS.txt
│   ├── Smart_Hospital_Ecosystem_Revolution.pdf
│   └── Unlocking_the_Smart_Hospital.mp4
│
└── QR Codes/                          # QR Codes
```

## 🎯 Kiến trúc Code

### **Separation of Concerns**
- **HTML**: Chỉ chứa cấu trúc và nội dung
- **CSS**: Tách biệt thành modules (main, components, pages)
- **JavaScript**: Tổ chức theo chức năng (app, charts, data-service)

### **CSS Organization**
1. **main.css**: Base styles, layout, animations
2. **components.css**: Reusable UI components
3. **pages/**: Page-specific styles (sẽ mở rộng sau)

### **JavaScript Modules**
1. **app.js**: Application initialization & PanZoom
2. **charts.js**: Chart.js configuration & management
3. **data-service.js**: API integration (Google Sheets)

## 🚀 Sử dụng

### **Development**
Chỉ cần mở file `index.html` trong trình duyệt:
```bash
# Windows
start index.html

# hoặc sử dụng Live Server extension trong VS Code
```

### **Production**
Để deploy lên server, upload toàn bộ thư mục và đảm bảo:
- Cấu trúc thư mục được giữ nguyên
- Tất cả đường dẫn tương đối hoạt động
- CDN resources có thể truy cập được

## 📦 Dependencies

### **External Libraries (CDN)**
- **TailwindCSS**: CSS framework
- **Alpine.js**: Reactive framework
- **Chart.js**: Biểu đồ
- **Panzoom**: Zoom & pan 3D viewer
- **Font Awesome**: Icons
- **Google Fonts**: Inter font family

### **APIs**
- **Google Sheets API**: Real-time housekeeping data

## 🔧 Configuration

### **Tailwind Config**
Cấu hình trong `index.html`:
```javascript
tailwind.config = {
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                scp: { 
                    bg: '#0f172a', 
                    card: '#1e293b', 
                    primary: '#0d9488', 
                    accent: '#22d3ee' 
                }
            }
        }
    }
}
```

### **Google Sheets API**
Cấu hình trong `assets/js/data-service.js`:
```javascript
const SHEETS_CONFIG = {
    SHEET_ID: '1_aMJkXZxN49COn9p2a64yNCtegPF1mlhL4M66q9JGfU',
    API_KEY: 'AIzaSyArA7XDisEHeSB3aiac7gv5F9KahiAZ0sU',
    RANGE: 'Sheet1!A2:G100'
};
```

## 🎨 Features

### **Dark/Light Mode**
- Toggle tự động
- Lưu preference
- Smooth transitions

### **Real-time Data**
- Google Sheets integration
- Auto-refresh mỗi 15 giây
- Live housekeeping logs

### **3D Facility Viewer**
- Pan & Zoom support
- Multiple layers (Architecture, Electric, Water, Fire)
- Interactive hotspots

### **Responsive Design**
- Mobile-first approach
- Breakpoints: sm, md, lg, xl
- Touch-friendly interface

## 🛠️ Maintenance

### **Thêm CSS mới**
1. Tạo file trong `assets/css/pages/` cho page-specific styles
2. Link trong HTML: `<link rel="stylesheet" href="assets/css/pages/your-page.css">`

### **Thêm JavaScript module**
1. Tạo file trong `assets/js/` hoặc `assets/js/components/`
2. Link trong HTML: `<script src="assets/js/your-module.js"></script>`
3. Export functions: `window.yourFunction = yourFunction;`

### **Cập nhật components**
1. Chỉnh sửa `assets/css/components.css` cho styles
2. Chỉnh sửa HTML markup trong các page

## 📝 Best Practices

1. ✅ **Luôn sử dụng đường dẫn tương đối**
2. ✅ **Comment code rõ ràng**
3. ✅ **Tách biệt concerns (HTML/CSS/JS)**
4. ✅ **Reuse components khi có thể**
5. ✅ **Test trên nhiều trình duyệt**
6. ✅ **Optimize images trước khi deploy**

## 📄 License
Copyright © 2026 SCP Hospital Management System

---

**Version**: 2.0  
**Last Updated**: 2026-01-06  
**Maintained by**: SCP Development Team
