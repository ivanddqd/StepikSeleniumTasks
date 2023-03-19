from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    b = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    sum = str(a + b)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(sum)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
