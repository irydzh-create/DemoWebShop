import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open website
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(5)

    # By XPath

    # 1. Register link
    register = driver.find_element(By.XPATH, "//a[@class='ico-register']")
    print("Register:", register.text)

    # 2. Login link
    login = driver.find_element(By.XPATH, "//a[@class='ico-login']")
    print("Login:", login.text)

    # 3. Product titles
    products = driver.find_elements(By.XPATH, "//h2[@class='product-title']")
    print("Products:", len(products))

    # 4. Search box
    search = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
    print("Search:", search.tag_name)

    # 5. Newsletter email
    newsletter = driver.find_element(By.XPATH, "//input[@id='newsletter-email']")
    print("Newsletter:", newsletter.tag_name)

    # 6. Shopping cart
    cart = driver.find_element(By.XPATH, "//li[@id='topcartlink']")
    print("Cart:", cart.text)

    # 7. Search input
    search_input = driver.find_element(By.XPATH, "//input[@name='q']")
    print("Search input:", search_input.tag_name)

    # 8. Poll radio buttons
    poll = driver.find_elements(By.XPATH, "//input[@name='pollanswers-1']")
    print("Poll answers:", len(poll))

    # 9. Wishlist link
    wishlist = driver.find_element(By.XPATH, "//a[@href='/wishlist']")
    print("Wishlist:", wishlist.text)

    # 10. Add to cart buttons
    buttons = driver.find_elements(By.XPATH, "//input[@value='Add to cart']")
    print("Add to cart:", len(buttons))

finally:
    driver.quit()