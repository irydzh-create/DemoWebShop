import time
from selenium import webdriver #Управление браузером
from selenium.webdriver.common.by import By #Стратегии поиска

driver = webdriver.Chrome()

try:#Выполнение действий

    # Open website
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(5)
    print("URL:", driver.current_url)
    print("Title:", driver.title)

    # By tag name         #Поиск элемента .find_element()
    div = driver.find_elements(By.TAG_NAME, "div")
    # By CSS selector
    div_1 = driver.find_elements(By.CSS_SELECTOR, "div")

    print("TAG_NAME div:", len(div))
    print("CSS_SELECTOR div:", len(div_1))

    a = driver.find_elements(By.TAG_NAME, "a")
    a_1 = driver.find_elements(By.CSS_SELECTOR, "a")

    print("TAG_NAME a:", len(a))
    print("CSS_SELECTOR a:", len(a_1))


    input_box=driver.find_elements(By.TAG_NAME, "input")
    input_box_1 = driver.find_elements(By.CSS_SELECTOR, "input")

    print("TAG_NAME input:", len(input_box))
    print("CSS_SELECTOR input:", len(input_box_1))


    img = driver.find_elements(By.TAG_NAME, "img")
    img_1 = driver.find_elements(By.CSS_SELECTOR, "img")

    print("TAG_NAME img:", len(img))
    print("CSS_SELECTOR img:", len(img_1))

    # img_js = driver.execute_script('return document.querySelectorAll("img").length')
    # print("JavaScript img:", img_js)
    ul = driver.find_elements(By.TAG_NAME, "ul")
    ul_1 = driver.find_elements(By.CSS_SELECTOR, "ul")

    print("TAG_NAME ul:", len(ul))
    print("CSS_SELECTOR ul:", len(ul_1))

    li = driver.find_elements(By.TAG_NAME, "li")
    li_1 = driver.find_elements(By.CSS_SELECTOR, "li")

    print("TAG_NAME li:", len(li))
    print("CSS_SELECTOR li:", len(li_1))


    span = driver.find_elements(By.TAG_NAME, "span")
    span_1 = driver.find_elements(By.CSS_SELECTOR, "span")

    print("TAG_NAME span:", len(span))
    print("CSS_SELECTOR span:", len(span_1))


    h2 = driver.find_elements(By.TAG_NAME, "h2")
    h2_1 = driver.find_elements(By.CSS_SELECTOR, "h2")

    print("TAG_NAME h2:", len(h2))
    print("CSS_SELECTOR h2:", len(h2_1))


    form = driver.find_elements(By.TAG_NAME, "form")
    form_1 = driver.find_elements(By.CSS_SELECTOR, "form")

    print("TAG_NAME form:", len(form))
    print("CSS_SELECTOR form:", len(form_1))


    body = driver.find_elements(By.TAG_NAME, "body")
    body_1 = driver.find_elements(By.CSS_SELECTOR, "body")

    print("TAG_NAME body:", len(body))
    print("CSS_SELECTOR body:", len(body_1))


finally:          #Завершение работы
    driver.quit() #Закрытие браузера



