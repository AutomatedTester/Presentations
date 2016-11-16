from selenium import webdriver
#f=webdriver.Firefox()
f=webdriver.Chrome()
f.get("http://localhost:8000/examples/example1.html")
element = f.find_element("id", "test1")
print "The the first html element visible? {}".format(element.is_displayed())

element.click()
