from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# РЕГИСТРАЦИЯ АККАУНТА

#driver.get("http://practice.automationtesting.in/")
# переход во вкладку My Account
#menu_my_account = driver.find_element_by_link_text("My Account")
#menu_my_account.click()

# заполнение поля Email address в разделе Register
#register_email_address = driver.find_element_by_id("reg_email")
#register_email_address.send_keys("emailqw@mail.ru")
#time.sleep(3)

# заполнение поля Password в разделе Register
#register_password = driver.find_element_by_id("reg_password")
#register_password.send_keys("Qw1234$$&&!!")
#time.sleep(3)

# нажатие на кнопку Register
#register_btn = driver.find_element_by_name("register")
#register_btn.click()
#time.sleep(3)



# ЛОГИН В СИСТЕМУ

driver.get("http://practice.automationtesting.in/")
# переход во вкладку My Account
menu_my_account = driver.find_element_by_link_text("My Account")
menu_my_account.click()

# заполнение поля Email address в разделе Login
login_email_address = driver.find_element_by_id("username")
login_email_address.send_keys("emailqw@mail.ru")
time.sleep(3)

# заполнение поля Password в разделе Login
login_password = driver.find_element_by_id("password")
login_password.send_keys("Qw1234$$&&!!")
time.sleep(3)

# нажатие на кнопку Login
login_btn = driver.find_element_by_name("login")
login_btn.click()
time.sleep(3)

# проверка наличия элемента "Logout"
element_logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation :nth-child(6)")
element_logout_get_text = element_logout.text
assert element_logout_get_text == "Logout"


driver.quit()