# ftp_uploader.py
from ftplib import FTP

def upload_to_ftp(file_path, remote_path):
    ftp = FTP("ftp.example.com")
    ftp.login("username", "password")

    with open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {remote_path}', file)

    ftp.quit()
