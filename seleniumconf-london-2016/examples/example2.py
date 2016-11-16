from selenium import webdriver
f=webdriver.Firefox()
f.get("http://localhost:8000/examples/example2.html")
print "The the first html element visible? {}".format(f.find_element("id", "test1").is_displayed())
