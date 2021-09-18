from selenium import webdriver
import time

navegator = webdriver.Chrome()


time.sleep(4)

navegator.get("https://www.ingresso.com/sao-paulo/home/cinemas/cinepolis-jk-iguatemi")

texto = navegator.find_element_by_xpath('//*[@id="contentarea-sessionpage"]/div[2]/section/div/div/ing-card-theater[1]/article/div/div[4]/ing-rooms/ul/li/ul/li[1]/a').click()

