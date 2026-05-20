
import os
import subprocess

ADS_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4896859041377751" crossorigin="anonymous"></script>'

def get_today_files():
    # Find files modified today (May 20, 2026)
    cmd = 'find /home/ubuntu/granahoje.github.io -name "*.html" -newermt 2026-05-20 ! -path "*/.*"'
    result = subprocess.check_output(cmd, shell=True).decode().splitlines()
    return result

def inject_ads(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if ADS_SCRIPT in content:
        return False
        
    if '</head>' in content:
        new_content = content.replace('</head>', f'    {ADS_SCRIPT}\n</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    files = get_today_files()
    count = 0
    for f in files:
        if inject_ads(f):
            count += 1
            print(f"✅ AdSense injected: {f}")
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    main()
