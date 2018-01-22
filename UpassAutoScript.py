from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
This Script Automatically Requests the UPASS for UBC Students
you just have to replace ubc_username(line 23) & ubc_password(line 27)
with your real ones. 

Also, you should have :
 - selenium installed
 - gecko driver downloaded and its Dir added to windows environment variable's PATH
 
Quick tip : you can add this script to your windows task scheduler and set the frequency accordingly
'''

#Instantiating the browser
browser = webdriver.Firefox()
browser.get("https://upassadfs.translink.ca/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2fupassbc.translink.ca%2ffs%2f&whr=https://shibboleth2.id.ubc.ca/idp/shibboleth&wfresh=1&wreply=https%3a%2f%2fupassbc.translink.ca%2ffs%2f") 
time.sleep(1)

#Finding the User-name and password fields
username = browser.find_element_by_id("j_username")
password = browser.find_element_by_id("password")

#Setting the User-name field
username.clear()
username.send_keys("ubc_username")

#Setting the Password field
password.clear()
password.send_keys("ubc_password")

#Submitting the UBC login form
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

try:
	#Checking the new month's check-box
	time.sleep(10)
	browser.find_element_by_id("chk_1").click()

	#Submitting the U-pass request
	browser.find_element_by_id("requestButton").click()

except:
	print("You already requested your UPass")

#Finally closing the browser
browser.close()
