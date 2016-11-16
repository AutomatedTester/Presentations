from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
from pdb import set_trace


def next_page(driver):
    driver.find_element(By.CSS_SELECTOR, '#next').click()
    sleep(.5)

driver = webdriver.Firefox()
driver.set_window_size(1200, 1025)
driver.get('http://futurepress.github.io/epub.js/reader/')
frame = WebDriverWait(driver, 5).until(ec.visibility_of_element_located([By.CSS_SELECTOR, 'iframe']))
for _ in range(5):
    next_page(driver)
driver.switch_to.frame(frame)

# Need to set overflow to visible on frame html element for this example to work
# NOTE: Be careful inspecting the browser after this, if you resize the epub it
# will re-apply the styling of overflow: hidden
# Alternatively, inspect browser before here
html = driver.find_element_by_css_selector('html')
driver.execute_script("return arguments[0].style.overflow='visible'", html)

# Color element red to prove it's not visible
element = driver.find_elements_by_css_selector('.block-rw')[6]
driver.execute_script("arguments[0].style.backgroundColor='red'", element)
set_trace()
print("Is the element displayed? {}".format(element.is_displayed()))


# Continue to the next page to show the element
driver.switch_to.default_content()
next_page(driver)
driver.switch_to.frame(frame)

# Prove this is the element we are using
driver.execute_script("arguments[0].style.backgroundColor='green'", element)

set_trace()

driver.quit()
