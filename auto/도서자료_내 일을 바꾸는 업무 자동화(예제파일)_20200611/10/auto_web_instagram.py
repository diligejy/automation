from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

opts = webdriver.ChromeOptions()
opts.add_argument('user-data-dir=' + './Chrome')
driver = webdriver.Chrome('chromedriver', options=opts)

try:
    driver.get('https://www.instagram.com')
    input()

    time.sleep(2)
    elem = driver.find_element_by_class_name('eyXLr')
    action = ActionChains(driver)
    action.move_to_element(elem)
    action.click()
    action.send_keys('#파이썬')
    action.perform()

    time.sleep(2)

    action = ActionChains(driver)
    action.move_by_offset(0, 50)
    action.click()
    action.perform()

    time.sleep(5)

    elem = driver.find_element_by_class_name('EZdmt')
    posts = elem.find_elements_by_class_name('_9AhH0')
    for post in posts:
        action = ActionChains(driver)
        action.move_to_element(post)
        action.click()
        action.perform()

        time.sleep(1)

        elem = driver.find_element_by_class_name('fr66n')
        svg = elem.find_element_by_tag_name('svg')
        if svg.get_attribute('aria-label') == '좋아요':
            action = ActionChains(driver)
            action.move_to_element(elem)
            action.click()
            action.perform()
            time.sleep(1)

        action = ActionChains(driver)
        action.send_keys(Keys.ESCAPE)
        action.perform()

        time.sleep(1)
        input()

except Exception as e:
    print(e)
finally:
    driver.quit()
