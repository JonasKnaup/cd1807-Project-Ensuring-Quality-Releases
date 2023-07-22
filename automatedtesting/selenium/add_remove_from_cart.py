# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# Start the browser and login with standard_user
def login (driver, user, password):
    
    driver.get('https://www.saucedemo.com/')
    print ('Login attempt, user: {},  password: {}'.format(user, password))
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    print('Clicking the login button')
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url
    print('User successfully logged in.')

def addAllProductsToCart(driver):
    print('Start adding all products to cart')
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print('Total products to add: {}'.format(len(products)))
    for product in products:
        productName = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        product.find_element(By.CLASS_NAME, "btn_inventory").click()
        print('Added {} to cart'.format(productName))
    cartBadgeText = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print('Cart badge text: {}'.format(cartBadgeText))
    assert len(products) == int(cartBadgeText)
    print('Product count equals cart badge count')
    print("Click on card button")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url
    print("Asserted cart page")
    cartElements = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cartElements) == len(products)
    print("All items are in the cart")

def removeAllProductsFromCart(driver):
    print('Start removing all products from cart')
    cartElements = driver.find_elements(By.CLASS_NAME, "cart_item")
    print('Total products to remove: {}'.format(len(cartElements)))
    for cartElement in cartElements:
        itemName = cartElement.find_element(By.CLASS_NAME, "inventory_item_name").text
        cartElement.find_element(By.CLASS_NAME, "cart_button").click()
        print('Removed {} from cart'.format(itemName))
    cartElements = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cartElements) == 0
    print("All items are removed from the cart")


def startTests():
    print('Starting the browser...')
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    print('Browser started successfully. Navigating to the demo page to login.')
    
    login(driver, 'standard_user', 'secret_sauce')
    addAllProductsToCart(driver)
    removeAllProductsFromCart(driver)

startTests()