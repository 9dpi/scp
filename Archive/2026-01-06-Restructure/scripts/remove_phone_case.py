"""
Script to remove phone case wrapper from HTML files
Converts phone-based mobile apps to responsive web apps
"""

import re
import os

def remove_phone_case(html_content):
    """Remove phone case styling and wrapper from HTML"""
    
    # Step 1: Remove phone-case specific CSS
    # Remove .phone-case style block
    html_content = re.sub(
        r'\.phone-case\s*\{[^}]+\}',
        '',
        html_content,
        flags=re.DOTALL
    )
    
    # Remove .notch style block
    html_content = re.sub(
        r'\.notch\s*\{[^}]+\}',
        '',
        html_content,
        flags=re.DOTALL
    )
    
    # Step 2: Update body styles
    # Replace centered body style with simpler version
    html_content = re.sub(
        r'body\s*\{[^}]+display:\s*flex;[^}]+\}',
        '''body {
            font-family: 'Inter', sans-serif;
            -webkit-user-select: none;
            user-select: none;
        }''',
        html_content,
        flags=re.DOTALL
    )
    
    # Step 3: Update .app-container styles
    # Replace flex-based container with max-width version
    html_content = re.sub(
        r'\.app-container\s*\{[^}]+\}',
        '''.app-container {
            max-width: 450px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
        }''',
        html_content,
        flags=re.DOTALL
    )
    
    # Step 4: Remove phone case and notch div wrappers from HTML
    # Remove <div class="phone-case" ...>
    html_content = re.sub(
        r'<div class="phone-case"[^>]*>',
        '',
        html_content
    )
    
    # Remove <div class="notch"></div>
    html_content = re.sub(
        r'<div class="notch"></div>',
        '',
        html_content
    )
    
    # Step 5: Update .app-container div class
    # Change from flex-based to simple styling
    html_content = re.sub(
        r'<div class="app-container[^"]*"[^>]*>',
        '<div class="app-container relative shadow-2xl overflow-hidden">',
        html_content
    )
    
    # Step 6: Update body class
    # Simpler body class
    html_content = re.sub(
        r'<body[^>]*class="[^"]*"[^>]*>',
        lambda m: '<body class="bg-slate-100" oncontextmenu="return false;" ' + 
                  ('x-init' in m.group(0) and re.search(r'x-init="[^"]*"', m.group(0)).group(0) or '') + '>',
        html_content
    )
    
    # Step 7: Remove extra closing </div> at the end (from phone-case wrapper)
    # Find last </div> before </body> and check if it's extra
    html_content = re.sub(
        r'</div>\s*</div>\s*(<script>)',
        r'</div>\n\n    \1',
        html_content
    )
    
    # Step 8: Update bottom-nav positioning
    # Change from absolute to fixed with proper positioning
    html_content = re.sub(
        r'\.bottom-nav\s*\{[^}]+\}',
        '''.bottom-nav {
            position: fixed;
            bottom: 0;
           left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 450px;
            height: 90px;
            z-index: 50;
        }''',
        html_content,
        flags=re.DOTALL
    )
    
    return html_content

# List of files to process
files_to_process = [
    'bacsy.html',
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
]

base_path = r'd:\Dropbox\Project\Smart Medial Connect\Hospital_Management\pages'

print("🔄 Bắt đầu xử lý files...")
print("=" * 50)

for filename in files_to_process:
    filepath = os.path.join(base_path, filename)
    
    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process content
        new_content = remove_phone_case(content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {filename} - Đã cập nhật")
        
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("=" * 50)
print("🎉 Hoàn tất!")
