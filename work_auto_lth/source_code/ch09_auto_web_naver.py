from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('./chromedriver')
xlsx = Workbook()
sheet = xlsx.active
sheet.append(['Title', 'Link', 'Published date'])

keyword = input("검색어를 입력하세요: ")

try:
    driver.get('https://naver.com/')
    elem = driver.find_element_by_id('query')
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    div = driver.find_element_by_class_name("_blogBase")
    #elem = div.find_element_by_tag_name("ul")
    blogs = div.find_elements_by_xpath('./ul/li')

    for blog in blogs:
        title_tag = blog.find_element_by_class_name('sh_blog_title')
        # 태그가 가진 title 속성값을 가져옴
        title = title_tag.get_attribute('title')
        # 만약 title 속성값이 없어서, 내용이 비어있을 경우에는
        if not title:
            title = title_tag.text
        
        link = title_tag.get_attribute('href')
        
        pub_date_tag = blog.find_element_by_class_name('txt_inline')

        sheet.append([title, link, pub_date_tag.text])   
    

except Exception as e:
    print(e)

finally:
    driver.quit()

file_name = 'result.xlsx'
xlsx.save(file_name)