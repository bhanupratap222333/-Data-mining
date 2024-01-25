from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune")
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="body"]/div[1]/div/div[2]/div[1]/div/div[1]/div').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="body"]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="body"]/div[1]/div/div[2]/div[1]/div/div[2]/div[3]').click()
time.sleep(2)
old_height = driver.execute_script("return document.body.scrollHeight")
time.sleep(2)

counter=1
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(counter)
    counter +=1
    print(old_height)
    print(new_height)
    if new_height == old_height:
        break
    old_height=new_height


html = driver.page_source

with open("magicbricksdataset.html" , "w" , encoding= "utf-8") as f:
    f.write(html)


