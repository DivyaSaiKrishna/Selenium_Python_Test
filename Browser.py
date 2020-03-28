from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
import pytest_html

browser = webdriver.Firefox()
print("Google Website Will Open")
browser.get('https://www.google.com/')

def thanos():
    print("Thanos character is entered in google search bar")
    inputElement = browser.find_element_by_name("q").send_keys("thanos character")
    time.sleep(5)
    browser.find_element_by_class_name("sbl1").click()
    time.sleep(5)
    #browser.find_element_by_class_name("IJOITb").click()
    #time.sleep(5)
    browser.find_element_by_class_name("c3yYr").click()
    print("Mission Infinity Gauntlet is Done")
    time.sleep(30)
def joey():
    browser.get('https://www.google.com/')
    time.sleep(5)
    inputElement = browser.find_element_by_name("q").send_keys("joey friends")
    time.sleep(5)
    browser.find_element_by_class_name("sbl1").click()
    time.sleep(5)
    #browser.find_element_by_class_name("TdUeNc AIOfFd").click()
    elm = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div[8]/div[1]/div[3]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/canvas')
    elm.click()
    print("Joey Tribbiani will eat Food")
    time.sleep(30)

thanos()
joey()