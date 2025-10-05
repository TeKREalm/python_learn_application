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
body = "這是一封由 Python 自動發送的郵件，幫助你提升效率！"

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

    


#
#✨ 技術解析：
#1. 設置 SMTP 伺服器：
#• 常用郵件服務的 SMTP 設定：
#• Gmail：smtp.gmail.com
#• Outlook（Office 365）：smtp.office365.com
#• Yahoo Mail：smtp.mail.yahoo.com
#2. 構建郵件內容：
#• 使用 MIMEText 和 MIMEMultipart，可以輕鬆添加主題、正文，甚至附件。
#3. 安全性建議：
#• 使用應用程式密碼代替郵箱密碼，提升帳號安全性。例如，Gmail 和 Outlook 都支持應用程式密碼功能。
#🔥 快速練習題：
#1. 批量發送郵件：
#• 使用清單存放多個收件人，通過迴圈完成批量郵件發送。
#2. 帶附件的郵件：
#• 嘗試將報表、圖片等文件作為附件添加到郵件中。
#3. 每日自動提醒：
#• 配合 schedule 模組，設置每日自動發送的提醒郵件。