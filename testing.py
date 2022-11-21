import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import requests
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.get("https://www.thesparksfoundationsingapore.org/")

print("\n \n************** Start checking TestCases *********************\n")

# TestCase 1:Title 
print("TestCase_1:")
if(driver.title):
    print("Successfully verified Testcase_1: ",driver.title)
else:
    print("Title Verification Failed!\n")
time.sleep(3)
print("")

# TestCase 2:Home button 
print("TestCase_2:")
try:
    driver.find_element(By.CLASS_NAME, "The Sparks Foundation").click()
    print("Successfully verified Testcase_2\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")
time.sleep(3)

# TestCase 3:Check if navbar appears
print("TestCase_3:")
try:
    driver.find_element(By.CLASS_NAME,"navbar").click()
    print("Successfully verified Testcase_3\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")
time.sleep(3)

# TestCase 4:Scrolling down 
print("TestCase_4:")
for i in range(0,1500,200):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("Successfully verified testcase_4")
print("")

# TestCase 5:scrolling up 
print("TestCase_5:")
driver.find_element(By.ID,"toTopHover").click()
time.sleep(1)
print("Successfully verified testcase_5")
print("")

# TestCase 6:About Us Page 
print("TestCase_6:")
try:
    driver.find_element(By.LINK_TEXT,'About Us').click()
    time.sleep(3)

    print('Successfully verified testcase_6\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)


# TestCase 7:Policies and Code Page 
print("TestCase_7:")
try:
    driver.find_element(By.LINK_TEXT,'Policies and Code').click()
    time.sleep(3)

    print('Successfully verified testcase_7\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 8:Workshop page 
print('TestCase_8:')
try:
    driver.find_element(By.LINK_TEXT,'Programs').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Workshops").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'LEARN MORE').click()
    time.sleep(3)
    print('Successfully verified testcase_8\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

## TestCase 9: Check If Logo Exists 
print('TestCase_9:')
try:
    driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
print("switched to 1st Tab\n")
time.sleep(1.5)

# TestCase 10:Check the Form
print("TestCase+10:")
try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(3)
    print("Typing name...")
    driver.find_element(By.NAME,'Name').send_keys('Kriti')
    time.sleep(3)
    print("Typing Email address...")
    driver.find_element(By.NAME,'Email').send_keys('kritidwivedikd111@gmail.com')
    time.sleep(3)
    select =Select(driver.find_element(By.CLASS_NAME,'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

# TestCase 11:Check the Contact us Page
print("TestCase_11:")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(1)
    info = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)
   
    
    if(info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')
   
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")


# TestCase 12:again back to main page

print("TestCase_12:")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/h1/a").click()
print(" again back to main page")
time.sleep(3)
print("")


# TestCase 13:clicking 1-6

print("TestCase_13:")

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[2]/a").click()
print(" clicked 2 internships ")
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[3]/a").click()
print(" clicked 3 Mentorship ")
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[4]/a").click()
print(" clicked 4 support ")
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a").click()
print(" clicked 5 scholarships ")
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/section/div/ol/li[6]/a").click()
print(" clicked 6 community ")
time.sleep(1)


driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
print("scrolled 500px")
print("")

# TestCase 14:iframe for youtube 

print("TestCase_14:")

required_frame = driver.find_element(By.XPATH,"//iframe[contains(@src,'https://www.youtube.com/embed/kgj_0E_urK0?autoplay=0&theme=light&loop=1&disablekb=1&modestbranding=1&hd=1&autohide=0&color=white&controls=0&showinfo=0&showsearch=0&cc_load_policy=1&rel=0')]")
driver.switch_to.frame(required_frame) 

element = driver.find_element(By.XPATH,"//button[@aria-label='Play']")
element.click()

print("YouTube video played")


time.sleep(10)
stop = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/video").click()
print("Pause Video\n")
time.sleep(1.5)


driver.refresh()
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print("page refreshed & Scrolled down\n")
time.sleep(4)

# TestCase 15:Jobs at Angel.co Portal 

print("TestCase_15:")

driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[2]/ul/li[2]/a").click()
print("Jobs at Angel.co Portal page:- Success\n")
time.sleep(10)

# TestCase 16:Jobs at Tech in Asia Portal 

print("TestCase_16:")

driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a").click()
print("Jobs at Tech in Asia Portal page:- Success\n")
time.sleep(10)


# TestCase 17:Code for India page 

print("TestCase_17:")

driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[1]/ul/li[3]/a").click()
print("Code for India page:- Success\n")
time.sleep(8)

# TestCase 18:Internships at Internshala 

print("TestCase_18:")


driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[3]/ul/li/a").click()
print("Internships at Internshala page:- Success\n")
time.sleep(5)