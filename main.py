from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
#options.add_experimental_option("excludeSwitches", ['enable-logging'])
options.add_argument(r"--user-data-dir=./chromeUserTwo")

path = r'C:\Users\toele\python-projects\chromedriver.exe'
driver = webdriver.Chrome(path, options=options)
driver.get('https://emeraldcity2residents.buildinglink.com/v2/tenant/amenities/availabilitygrid.aspx')

#time = driver.find_elements_by_class_name('ReservationGridRowHeader-Inner')
#avail = driver.find_elements_by_class_name('ReservationGridCell-Inner')
#
#for i in range(len(time)):
#    print(str(i) + ' ' + time[i].text + ' ' + avail[i].text)
