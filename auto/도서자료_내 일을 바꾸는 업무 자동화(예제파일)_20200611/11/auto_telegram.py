import telegram
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')

msg = ''
try:
    driver.get('https://naver.com')
    
    elem = driver.find_element_by_id('query')
    elem.send_keys('파이썬')
    elem.send_keys(Keys.RETURN)

    div = driver.find_element_by_class_name('_blogBase')
    blogs = div.find_elements_by_xpath('./ul/li')
    for blog in blogs:
        title_tag = blog.find_element_by_class_name('sh_blog_title')
        msg += title_tag.text + '\n'

except Exception as e:
    print(e)
finally:
    driver.quit()

token = '962058964:AAG5G53iMXjqjHWPE8d17FDgnE0lC_-pnhA'
bot = telegram.Bot(token)
bot.send_message(57841042, msg)
