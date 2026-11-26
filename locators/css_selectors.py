import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open site
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(5)

    # By class name

    # 1. Register link
    register = driver.find_element(By.CLASS_NAME, "ico-register")
    print("Register:", register.text)

    # 2. Login link
    login = driver.find_element(By.CLASS_NAME, "ico-login")
    print("Login:", login.text)

    # 3. Product titles
    products = driver.find_elements(By.CLASS_NAME, "product-title")
    print("Products:", len(products))

    # By ID

    # 4. Search box
    search = driver.find_element(By.ID, "small-searchterms")
    print("Search:", search.tag_name)

    # 5. Newsletter email
    newsletter = driver.find_element(By.ID, "newsletter-email")
    print("Newsletter:", newsletter.tag_name)

    # 6. Shopping cart
    cart = driver.find_element(By.ID, "topcartlink")
    print("Cart:", cart.text)

    # By Name

    # 7. Search input
    search_input = driver.find_element(By.NAME, "q")
    print("Search input:", search_input.tag_name)

    # 8. Poll radio buttons
    poll = driver.find_elements(By.NAME, "pollanswers-1")
    print("Poll answers:", len(poll))

    # By Attribute

    # 9. Wishlist link
    wishlist = driver.find_element(By.CSS_SELECTOR, "a[href='/wishlist']")
    print("Wishlist:", wishlist.text)

    # 10. Add to cart buttons
    buttons = driver.find_elements(By.CSS_SELECTOR, "input[value='Add to cart']")
    print("Add to cart:", len(buttons))

finally:
    driver.quit()