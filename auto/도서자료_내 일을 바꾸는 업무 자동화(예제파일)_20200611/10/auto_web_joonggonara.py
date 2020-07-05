from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('http://cafe.naver.com/joonggonara')

    elem = driver.find_element_by_id('topLayerQueryInput')
    elem.send_keys('자전거')
    elem.send_keys(Keys.RETURN)
    
    iframe = driver.find_element_by_id('cafe_main')
    driver.switch_to.frame(iframe)

    elem = driver.find_elements_by_class_name('article-board')[1]
    rows = elem.find_elements_by_xpath('./table/tbody/tr')
    for row in rows:
        elem = row.find_element_by_class_name('article')
        print(elem.text)

except Exception as e:
    print(e)
finally:
    driver.quit()
