import os
import hashlib
import re
import socket

def get_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def calculate_file_hash(file_path, hash_algorithm):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def is_malicious_code_present(file_path, malicious_patterns):
    with open(file_path, 'r', errors='replace') as f:
        content = f.read()
        for pattern in malicious_patterns:
            if re.search(pattern, content):
                return True
    return False

def scan_open_ports(target_host, port_range):
    open_ports = []
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == '__main__':
    directory_to_check = 'path/to/your/directory'
    files = get_files_in_directory(directory_to_check)
    target_host = '127.0.0.1'  # 대상 호스트 IP 주소
    hash_algorithm = 'sha512'   # 더 강력한 해시 알고리즘 선택
    malicious_patterns = [r"malicious_pattern1", r"malicious_pattern2"]
    port_range = range(1, 1025)  # 스캔할 포트 범위

    no_malicious_found = True
    
    for file_path in files:
        hash_value = calculate_file_hash(file_path, hash_algorithm)
        is_malicious = is_malicious_code_present(file_path, malicious_patterns)
        open_ports = scan_open_ports(target_host, port_range)
        
        print(f'File: {file_path}')
        print(f'File Hash ({hash_algorithm}): {hash_value}')
        
        if is_malicious:
            print('Malicious code detected!')
            no_malicious_found = False
        else:
            print('No malicious code found.')
            
        if open_ports:
            print(f'Open ports on {target_host}: {open_ports}')
        
    if no_malicious_found:
        print('No malicious files detected in the directory.')

# 악성코드 감지