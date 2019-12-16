from tkinter import *
from tkinter import ttk
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
import os


username = 'Test Bot'

url = 'URL GOES HERE'
workingdir = os.getcwd()
driver = webdriver.Firefox(executable_path=workingdir+"\Resources\geckodriver.exe")
driver.get(url)

box = driver.find_element_by_name('username')
check = driver.find_element_by_css_selector("input[type='checkbox']")
###
box.send_keys(username)
check.click()
signup = driver.find_element_by_css_selector("button[type='submit']")
signup.click()
