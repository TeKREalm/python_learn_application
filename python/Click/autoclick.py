
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com/?hl=zh_TW')
#開啟首頁

driver.implicitly_wait(6)
#等待網站載入(最多等6秒
driver.find_element(By.XPATH, '//*[@id="gb"]/div[1]/div[2]/a').click()
#driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/div/div[2]/a').click()
#點擊「圖片」，就是貼上剛剛複製的xpath

print("請按下 Enter 繼續...")
input()
print("繼續執行。")




"""

#二、雙擊（左鍵點兩下）
from selenium import webdriver
from selenium.webdriver import ActionChains
#再多import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.google.com/')
driver.implicitly_wait(6)
dc =driver.find_element_by_xpath('//*[@id="gbwa"]/div/a')
ActionChains(driver).double_click(dc).perform()

"""