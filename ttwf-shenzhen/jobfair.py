from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    firefox = webdriver.Firefox()
    for i in range(1000):
        firefox.get('http://www.w3.org/TR/webdriver/')
        time.sleep(2)
        firefox.find_element_by_link_text('9. Elements').click()
        time.sleep(2)
        firefox.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        time.sleep(2)
        firefox.find_element_by_link_text("CSS Selectors API").click()
        time.sleep(2)
    firefox.quit()

if __name__ == '__main__':
    main()
