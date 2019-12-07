#Нахождение страницы вк по лицу
#Необходимо заполнить логин и пароль в строках 23,24
from selenium import webdriver
from threading import Thread
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time 
driver = webdriver.Chrome() 
driver.get("https://findmevk.ru/") 
elem=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/input').send_keys('C://Users/qwe/Desktop/Xakaton/test.jpg')
time.sleep(4)
elem=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[3]/div[2]/div/div')
elem.click()
time.sleep(4)
elem=driver.page_source
soup=BeautifulSoup(elem,'lxml')
elem=soup.find_all('div',class_='resultContainer')
Vk_Person_Url=elem[1].find('a').get('href')
Vk_Person_Url=Vk_Person_Url[2:]
Vk_Person_Url="https://"+Vk_Person_Url
driver.get(Vk_Person_Url) 
elem=driver.find_element_by_xpath('//*[@id="quick_email"]').send_keys('логин от вк')
elem=driver.find_element_by_xpath('//*[@id="quick_pass"]').send_keys('Пароль от вк')
elem=driver.find_element_by_xpath('//*[@id="quick_login_button"]')
elem.click()
print('Собираем список последних аудиозаписей и сообществ')
