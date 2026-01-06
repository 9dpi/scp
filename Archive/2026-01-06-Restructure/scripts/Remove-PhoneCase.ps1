# PowerShell script to remove phone case wrapper from HTML files
# Run this in: d:\Dropbox\Project\Smart Medial Connect\Hospital_Management\pages

$files = @(
    'benh_nhan.html',
    'bep.html',
    'dieuduong.html',
    'kehoach_tonghop.html',
    'kho.html',
    'laixe_capcuu.html',
    'nhanvien_kythat_thietbi.html',
    'quanly.html',
    'quanly_chatluong.html',
    'anninh_baove.html'
)

Write-Host "🔄 Bắt đầu xử lý files..." -ForegroundColor Cyan
Write-Host "=" * 60

foreach ($file in $files) {
    try {
        $content = Get-Content $file -Raw -Encoding UTF8
        
        # Backup
        $backupFile = $file -replace '\.html$', '.backup.html'
        $content | Out-File $backupFile -Encoding UTF8
        
        # Step 1: Remove CSS blocks
        $content = $content -replace '(?s)body\s*\{[^}]*background:\s*#e2e8f0[^}]*\}', @'
body {
            font-family: 'Inter', sans-serif;
            -webkit-user-select: none;
            user-select: none;
        }
'@
        
        $content = $content -replace '(?s)\.phone-case\s*\{[^}]*\}', ''
        $content = $content -replace '(?s)\.notch\s*\{[^}]*\}', ''
        
        $content = $content -replace '(?s)\.app-container\s*\{[^}]*overflow:\s*hidden;[^}]*\}', @'
.app-container {
            max-width: 450px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
        }
'@
        
        $content = $content -replace '(?s)\.bottom-nav\s*\{[^}]*position:\s*absolute[^}]*\}', @'
.bottom-nav {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 450px;
            height: 90px;
            z-index: 50;
        }
'@
        
        # Step 2: Remove HTML wrappers
        $content = $content -replace '<body[^>]*class="[^"]*"[^>]*>', '<body class="bg-slate-100" oncontextmenu="return false;">'
        $content = $content -replace '<div class="phone-case"[^>]*>', ''
        $content = $content -replace '<div class="notch"></div>\s*', ''
        
        # Step 3: Update app-container div
        $content = $content -replace '<div class="app-container[^"]*"[^>]*>', '<div class="app-container relative shadow-2xl overflow-hidden transition-colors duration-300" :class="darkMode ? ''bg-[#030712]'' : ''bg-slate-50''">'
        
        # Step 4: Remove extra closing div
        $content = $content -replace '</div>\s*</div>\s*(<script>)', "</div>`n`n    `$1"
        
        # Save
        $content | Out-File $file -Encoding UTF8 -NoNewline
        
        Write-Host "✅ $file - Đã cập nhật" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ $file - Lỗi: $_" -ForegroundColor Red
    }
}

Write-Host "=" * 60
Write-Host "🎉 Hoàn tất!" -ForegroundColor Green
Write-Host "Backup files: *.backup.html" -ForegroundColor Yellow
