import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage                  #可以mail圖片
from pathlib import Path                                #使用路徑lib

import os

# 發件人與收件人 ###這邊要user改，使用gmail發信到其他mail
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@example.com"
password = "password"
# 設定郵件內容
subject = "Python 自動化郵件"
body = "這是一封由 Python 自動發送的郵件，請撰寫內容！"

# 建立郵件對象
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain")) #郵件內容

print(os.getcwd())
message.attach(MIMEImage(Path('C:/Users/user/Desktop/python_test/Email/aespa.png').read_bytes()))  # 可以mail圖片->郵件圖片內容

# 連接郵件伺服器並發送
try:
    #with smtplib.SMTP("smtp.office365.com", 587) as server: # 使用 Microsoft Outlook 的 SMTP 伺服器
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server: # 使用 Gmail 的 SMTP 伺服器
        server.starttls()                                           # 啟用 TLS 安全加密
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("郵件發送成功！")
except Exception as e:
        print(f"郵件發送失敗：{e}")

    



#1. 設置 SMTP 伺服器：
#• 常用郵件服務的 SMTP 設定：
#• Gmail：smtp.gmail.com
#• Outlook（Office 365）：smtp.office365.com
#• Yahoo Mail：smtp.mail.yahoo.com
