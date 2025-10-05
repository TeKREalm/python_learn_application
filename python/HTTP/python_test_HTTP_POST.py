import requests
print(requests.__version__)



print("Hello python Ken")


# 定義目標 URL
url = "https://httpbin.org/post"  # 這裡使用 httpbin.org 來測試 POST 請求

# 要發送的資料，以字典格式表示
payload = {
    'key1': 'value1',
    'key2': 'value2'
}

# 發送 POST 請求，並將資料傳遞給 data 參數
response = requests.post(url, data=payload)

# 檢查請求是否成功
if response.status_code == 200:
    # 獲取回應內容
    print("POST 請求成功：")
    print(response.text)  # .text 屬性會返回回應的文字內容
else:
    print(f"POST 請求失敗，狀態碼：{response.status_code}")
