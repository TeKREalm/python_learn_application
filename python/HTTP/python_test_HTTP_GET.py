import requests
print(requests.__version__)

print("Hello python Ken")


# 定義目標 URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# 發送 GET 請求並獲取回應
response = requests.get(url)

# 檢查請求是否成功 (狀態碼 200 代表成功)
if response.status_code == 200:
    # 獲取回應內容 (通常是 JSON 格式，可以用 .json() 轉換)
    data = response.json()
    print("GET 請求成功：")
    print(data)
else:
    print(f"GET 請求失敗，狀態碼：{response.status_code}")