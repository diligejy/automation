import time
from selenium import webdriver
from datetime import datetime, timedelta
from my_email import send_mail

today = datetime.now()
diff = timedelta(days=7)
base_date = today - diff
base_date = base_date.strftime('%Y.%m.%d.')
cron_base = './notice'
opts = webdriver.ChromeOptions()
opts.add_argument('headless')
opts.add_argument('window-size=1920,1080')
driver = webdriver.Chrome('chromedriver', options=opts)

try:
    keywords = open(cron_base+'/keywords.txt', 'r').readlines()
    matches = []

    driver.get('https://www.msit.go.kr/web/msipContents/contents.do?mId=MTAzMA==')
    time.sleep(1)
    elems = driver.find_elements_by_xpath("//div[@class='board_list']/div/a")
    for elem in elems:
        title_tag = elem.find_element_by_class_name('title')
        date_tag = elem.find_element_by_class_name('date')
       
        if date_tag.text > base_date:
            for k in keywords:
                if k.strip() in title_tag.text:
                    matches.append(f'{date_tag.text}: {title_tag.text}')
                    break

    if matches:
        contents = '최근 올라온 공고가 있습니다.\n\n'

        contents += '\n'.join(matches)
        send_mail('이태화', 'alghost.lee@gmail.com', contents)

except Exception as e:
    print(e)
finally:
    driver.quit()
