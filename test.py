from typing import TextIO
from selenium import webdriver
from datetime import datetime
import selenium.webdriver.chrome.service as service

service = service.Service('C:/chromedriver.exe')
service.start()

sysTime = datetime.strftime(datetime.now(), "%H:%M")                         # системное время с точностью до минут
sysTimeSec = datetime.strftime(datetime.now(), "%H:%M:%S")                   # системное время с точностью до секунд

driver = webdriver.Remote(service.service_url)
driver.get('https://yandex.ru/time/')                                        # открываем страницу


f: TextIO = open("log.txt",  "w", encoding='utf-8')                          # открываем файл для записи

if sysTime in driver.title:                                                  # проверяем есть ли системное время в title
    f.write(sysTimeSec + " — УСПЕХ: " + sysTime + "=" + driver.title[0:5])  # записываем результат проверки
else:
    f.write(sysTimeSec + " — ОШИБКА: " + sysTime + "≠" + driver.title[0:5])


f.close()                                                                    # закрываем файл