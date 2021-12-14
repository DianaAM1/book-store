from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Users\Пользователь\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.11.4_0'
chrome_options = Options()
chrome_options.add_argument('load-extension='+path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)

driver.get("http://practice.automationtesting.in/")


# переход во вкладку My Account
#menu_my_account = driver.find_element_by_link_text("My Account")
#menu_my_account.click()

# заполнение поля Email address в разделе Login
#login_email_address = driver.find_element_by_id("username")
#login_email_address.send_keys("emailqw@mail.ru")
#time.sleep(3)

# заполнение поля Password в разделе Login
#login_password = driver.find_element_by_id("password")
#login_password.send_keys("Qw1234$$&&!!")
#time.sleep(3)

# нажатие на кнопку Login
#login_btn = driver.find_element_by_name("login")
#login_btn.click()
#time.sleep(3)

# переход во вкладку Shop
menu_shop = driver.find_element_by_link_text("Shop")
menu_shop.click()

# ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА

# выбор книги HTML5 Forms
#book_html5forms = driver.find_element_by_css_selector(".post-181 h3")
#book_html5forms.click()
# проверка заголовка книги HTML5 Forms
#book_html5forms_heading = driver.find_element_by_css_selector(".summary h1")
#book_html5forms_heading_get_text = book_html5forms_heading.text
#assert book_html5forms_heading_get_text == "HTML5 Forms"

# КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ

# выбор категории "HTML"
#category_html = driver.find_element_by_css_selector(".cat-item-19 a")
#category_html.click()
#time.sleep(3)
# проверка наличия трех элементов на странице "HTML"
#number_book_elements = driver.find_elements(By.CLASS_NAME, "product")
#print(number_book_elements)
#assert len(number_book_elements) == 3


# СОРТИРОВКА ТОВАРОВ

# проверка выбора в селекторе варианта сортировки по умолчанию
#sort_element = driver.find_element_by_css_selector("[value='menu_order']")
#sort_element_selected = sort_element.get_attribute("selected")
#print("Value of sorting:", sort_element_selected)
#if sort_element_selected is None:
#    print("В селекторе не выбран вариант сортировки Default sorting")
#else:
#    print("В селекторе выбран вариант сортировки Default sorting")


# выбор в селекторе варианта сортировки от большего к меньшему
#sort_element_high_to_low = driver.find_element_by_class_name("orderby")
#select = Select(sort_element_high_to_low)
#select.select_by_value("price-desc")

# проверка выбора в селекторе варианта сортировки от большего к меньшему
#sort_element_high_to_low = driver.find_element_by_css_selector("[value='price-desc']")
#sort_element_high_to_low_selected = sort_element_high_to_low.get_attribute("selected")
#print("Value of sorting:", sort_element_high_to_low_selected)
#if sort_element_selected is None:
#    print("В селекторе не выбран вариант сортировки Sort by price: High to low")
#else:
#    print("В селекторе выбран вариант сортировки Sort by price: High to low")


# ОТОБРАЖЕНИЕ, СКИДКА ТОВАРА

# выбор книги "Android Quick Start"
#book_android_quick_start = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
#book_android_quick_start.click()

# проверка старой цены книги "Android Quick Start"
#old_price_book_android_quick_start = driver.find_element_by_tag_name("del")
#old_price_book_android_quick_start_get_text = old_price_book_android_quick_start.text
#assert "600.00" in old_price_book_android_quick_start_get_text
# проверка новой цены книги "Android Quick Start"
#new_price_book_android_quick_start = driver.find_element_by_css_selector("ins .amount")
#new_price_book_android_quick_start_get_text = new_price_book_android_quick_start.text
#assert "450.00" in new_price_book_android_quick_start_get_text

# открытие окна предпросмотра картинки книги
#book_img_open = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")))
#book_img_open.click()

# закрытие окна предпросмотра картинки книги
#book_img_close_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
#book_img_close_btn.click()


# ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ

# добавление товара в корзину
#book_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
#book_add_to_basket_btn.click()
#time.sleep(3)

# проверка количества товаров в корзине и стоимости
#basket_item = driver.find_element_by_class_name("cartcontents")
#basket_item_get_text = basket_item.text
#assert basket_item_get_text == "1 Item"
#basket_cost = driver.find_element_by_css_selector(".menu-item .amount")
#basket_cost_get_text = basket_cost.text
#assert "180.00" in basket_cost_get_text

# переход в корзину
#basket = driver.find_element_by_id("wpmenucartli")
#basket.click()
# проверка значения Subtotal и Total
#basket_subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "180.00"))
#basket_total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), "189.00"))


# РАБОТА В КОРЗИНЕ

# скроллинг страницы вниз на 300 пикселей
#driver.execute_script("window.scrollBy(0, 300);")

# добавление товара в корзину
#book_1_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
#book_1_add_to_basket_btn.click()
#time.sleep(5)
#book_2_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='180']")
#book_2_add_to_basket_btn.click()
#time.sleep(5)
# переход в корзину
#basket = driver.find_element_by_id("wpmenucartli")
#basket.click()
#time.sleep(5)
# удаление первой книги
#book_1_delete_btn = driver.find_element_by_css_selector("[data-product_id='182']")
#book_1_delete_btn.click()
#time.sleep(5)
# отмена удаления первой книги
#undo = driver.find_element_by_link_text("Undo?")
#undo.click()
#time.sleep(5)
# увеличение количества товаров в корзине
#book_2_quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
#book_2_quantity.clear()
#time.sleep(5)
#book_2_quantity.send_keys("3")
#time.sleep(5)
# нажатие на кнопку "UPDATE BASKET"
#update_basket_btn = driver.find_element_by_name("update_cart")
#update_basket_btn.click()
#time.sleep(5)
# проверка количества товара в корзине (вторая книга)
#book_2_quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
#book_2_quantity_check = book_2_quantity.get_attribute("value")
#time.sleep(5)
#assert book_2_quantity_check == "3"
#time.sleep(5)

# нажатие на кнопку "APPLY COUPON"
#apply_coupon_btn = driver.find_element_by_name("apply_coupon")
#apply_coupon_btn.click()
#time.sleep(5)

# появление сообщения : "Please enter a coupon code"
#message = driver.find_element_by_class_name("woocommerce-error")
#message_get_text = message.text
#time.sleep(5)
#assert message_get_text == "Please enter a coupon code."


# ПОКУПКА ТОВАРА

# скроллинг страницы вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")

# добавление товара в корзину
book_1_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
book_1_add_to_basket_btn.click()
time.sleep(5)

# переход в корзину
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
time.sleep(5)

# нажатие на кнопку "PROCEED TO CHECKOUT"
procced_to_checkout_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
procced_to_checkout_btn.click()
time.sleep(5)

# заполнение обязательных полей
first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Jhon")
time.sleep(3)

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Jhonson")
time.sleep(3)

email_address = driver.find_element_by_id("billing_email")
email_address.send_keys("JJ@yandex.ru")
time.sleep(3)

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("1234567")
time.sleep(3)

country = driver.find_element_by_id("select2-chosen-1")
country.click()
time.sleep(3)
country_input = driver.find_element_by_id("s2id_autogen1_search")
country_input.send_keys("Russia")
time.sleep(3)
country_selection = driver.find_element_by_class_name("select2-match")
country_selection.click()
time.sleep(3)

address = driver.find_element_by_id("billing_address_1")
address.send_keys("Nevsky Prospekt, 1")
time.sleep(3)

city = driver.find_element_by_id("billing_city")
city.send_keys("Saint-Petersburg")
time.sleep(3)

state_country = driver.find_element_by_id("billing_state")
state_country.send_keys("Russia")
time.sleep(3)

postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("111111")
time.sleep(3)

# выбор способа оплаты
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
time.sleep(3)

# нажатие кнопки "PLACE ORDER"
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
time.sleep(5)

# появление сообщения : "Thank you. Your order has been received."
message = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# проверка отображения : "Check Payments"
check_payments_check = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3)"), "Check Payments"))


driver.quit()