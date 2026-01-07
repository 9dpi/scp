# SCP Ecosystem - Development Checkpoint (2026-01-07)

## 1. Project Structure Status
- **SCP Landing Page**: `index.html` (Root) - Restored original UI with App Cards and Hero Section.
- **HMIS Dashboard**: `hmis.html` - Dedicated Hospital Management Dashboard.
- **Housekeeping Mobile App**: `Archive/Legacy_Web_App/mobile/house_keeping.html` - Production-ready logic.

## 2. Key Features Completed (Housekeeping Module)
- **Workflow**: Scan QR -> Verify PIN -> Capture Photo -> Submit Report -> Live Dashboard Update.
- **QR Scanning**:
  - Implemented `Html5Qrcode` for camera access.
  - **Mapping Logic**: Automatically maps scanned URLs (Col B) to Location Names (Col A) using data from Google Sheet `QR_Code` tab.
- **Security**:
  - **PIN Verification**: Requires 4-digit PIN (from Sheet Col C or Master PIN `2026`/`8888`) to validate location.
- **Data Submission**:
  - Replaced `n8n` webhook with **Google Apps Script Web App** end-point.
  - Enables direct image upload to Google Drive and logging to Google Sheets.
- **Testing Support**:
  - Created `Archive/Legacy_Web_App/mobile/print_qr.html` for printing test QR codes.
  - Hidden "Manual Location Selector" to enforce QR scanning workflow.

## 3. Configuration Details
- **Google Sheet ID**: `1_aMJkXZxN49COn9p2a64yNCtegPF1mlhL4M66q9JGfU`
- **GAS Web App URL**: `https://script.google.com/macros/s/AKfycbyOtUQYPTzDWMzU_QK021ckJyDbt-lRLac7x1cwX0U6e3mcwLor4PC4LKxvJp5s0lzR/exec`
- **QR Code Sheet Name**: `QR_Code`

## 4. Pending / Next Steps
- Waiting for **Client Feedback** on the Housekeeping flow.
- Implementation of the **Security Module** (An ninh Bảo vệ) across the ecosystem.
- Refinement of the **Staff Management** portal.

## 5. Verified Deployed URLs (Live)
- **SCP Hub**: [https://9dpi.github.io/scp/](https://9dpi.github.io/scp/)
- **HMIS Dashboard**: [https://9dpi.github.io/hmis/](https://9dpi.github.io/hmis/)
- **Housekeeping Live Feed**: [https://9dpi.github.io/hmis/desktop/housekeeping.html](https://9dpi.github.io/hmis/desktop/housekeeping.html)

---
### Section 7: Final Layout Polish (Verified)
- [x] **Sidebar Scroll**: Fix menu bị cắt bằng `min-h-0` và `overflow-y-auto`.
- [x] **Content Stability**: Fix lỗi trôi màn hình bằng `flex-col` và reset `scrollTop`.
- [x] **UI Hygiene**: Thêm ảnh placeholder cho các báo cáo thiếu ảnh/ảnh lỗi.

---
**Timestamp**: 2026-01-07 22:00 (Local Time)
