from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def click():
    cookie = driver.find_element(By.CSS_SELECTOR, value="div#cookie")
    cookie.click()


def upgrade(price):
    time_machine = driver.find_element(By.CSS_SELECTOR, value="div[id='buyTime machine']")
    portal = driver.find_element(By.CSS_SELECTOR, value="div#buyPortal")
    alchemy_lab = driver.find_element(By.CSS_SELECTOR, value="div[id='buyAlchemy lab']")
    shipment = driver.find_element(By.CSS_SELECTOR, value="div#buyShipment")
    mine = driver.find_element(By.CSS_SELECTOR, value="div#buyMine")
    factory = driver.find_element(By.CSS_SELECTOR, value="div#buyFactory")
    grandma = driver.find_element(By.CSS_SELECTOR, value="div#buyGrandma")
    cursor = driver.find_element(By.CSS_SELECTOR, value="div#buyCursor")

    upgrades = [cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]
    upgrades[price].click()


def check_price():
    money = int(driver.find_element(By.CSS_SELECTOR, value="div#money").text.replace(",", ""))
    upgrade_prices_tags = driver.find_elements(By.CSS_SELECTOR, value="div#store b")
    upgrade_prices = [int(upgrade_prices_tags[i].text.split('- ')[1].replace(",", "")) for i in range(8)]
    return money, upgrade_prices


# tinker the strat (adding ratio):
def ultimate_strategy(upgrade_prices, ratio):
    if upgrade_prices[0] * 80 * ratio > upgrade_prices[3] and upgrade_prices[1] * 20 * ratio > upgrade_prices[3] and \
            upgrade_prices[2] * 4 * ratio > upgrade_prices[3]:
        return 3
    elif upgrade_prices[0] * 20 * ratio > upgrade_prices[2] and upgrade_prices[1] * 5 * ratio > upgrade_prices[2]:
        return 2
    elif upgrade_prices[0] * 4 * ratio > upgrade_prices[1]:
        return 1
    else:
        return 0


def check_money(money, next_upgrade_price):
    if money >= next_upgrade_price:
        return True


def score():
    cps = driver.find_element(By.CSS_SELECTOR, value="div#cps")
    print(cps.text)


# works:
def game(ratio):
    start_time = time.time()
    duration_seconds = 10
    end_time = start_time + duration_seconds

    while time.time() < end_time:
        click()
        next_upgrade = ultimate_strategy(check_price()[1], ratio)
        if check_money(check_price()[0], next_upgrade):
            upgrade(next_upgrade)

    score()
    print(f"Money: {check_price()[0]}")
    print(f"Ratio: {ratio}")
    driver.quit()

