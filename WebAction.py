from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

##### config
sleeptime = 40
#####

''' sample of selenium
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title,"Not Found Target Text in Web Title" 
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source,"No results found."
time.sleep(10)
driver.close()
'''

#    Open Web browser
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#    go to Google image
driver.get("https://images.google.com/")

#    Check the website is your target , should enter your title of target site
assert "Google" in driver.title,"Not Found Target Text in Web Title"

#    operation that you want on WebSite
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Taiwan")
elem.send_keys(Keys.RETURN)

elem = driver.find_elements_by_class_name("rg_ic")
Base64Straing = elem[10].get_attribute("src")
import Process64 as P64
P64.Show_Google(Base64Straing)



print "Ending Process after %d sec" % (sleeptime)
time.sleep(sleeptime)
driver.close()
