from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

# ДОБАВЛЕНИЕ КОММЕНТАРИЯ

# скроллинг страницы вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# выбор книги
time.sleep(3)
selenium_ruby_book = driver.find_element_by_css_selector(".post-160 h3")
selenium_ruby_book.click()
# скроллинг страницы, переход во вкладку Reviews
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
reviews_tab = driver.find_element_by_class_name("reviews_tab")
reviews_tab.click()
time.sleep(3)
# 5 звезд
star_5 = driver.find_element_by_class_name("star-5")
star_5.click()
time.sleep(3)
# заполнение поля Review
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
time.sleep(3)
# name
name = driver.find_element_by_id("author")
name.send_keys("Name")
time.sleep(3)
# email
email = driver.find_element_by_id("email")
email.send_keys("Email@mail.ru")
time.sleep(3)
# нажатие на кнопку Submit
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
time.sleep(5)


driver.quit()