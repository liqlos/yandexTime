from typing import TextIO
from selenium import webdriver
from datetime import datetime
import selenium.webdriver.chrome.service as service

service = service.Service('C:/chromedriver.exe')
service.start()

driver = webdriver.Remote(service.service_url)
driver.get('https://yandex.ru/time/')                                        # открываем страницу


f: TextIO = open("log.txt",  "w", encoding='utf-8')                          # открываем файл для записи

if datetime.strftime(datetime.now(), "%H:%M")in driver.title:                # проверяем есть ли системное время в title
    f.write(datetime.strftime(datetime.now(), "%H:%M:%S") + " — УСПЕХ: " + datetime.strftime(datetime.now(), "%H:%M")+ "=" + driver.title[0:5])
else:                                                                        # записываем результат проверки
    f.write(datetime.strftime(datetime.now(), "%H:%M:%S") + " — ОШИБКА: " + datetime.strftime(datetime.now(), "%H:%M")+ "≠" + driver.title[0:5])


f.close()                                                                    # закрываем файл
service.stop()                                                               # останавливаем Chromedriver