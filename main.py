from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from time import strftime
import re

options = Options()
#options.add_experimental_option("excludeSwitches", ['enable-logging'])
options.add_argument(r"--user-data-dir=C:/Users/toele/chromeProfiles/chromeUserOne")

path = r'C:\Users\toele\python-projects\chromedriver.exe'
driver = webdriver.Chrome(path, options=options)
driver.get('https://emeraldcity2residents.buildinglink.com/v2/tenant/Amenities/AvailabilityGrid.aspx')

time = driver.find_elements_by_class_name('ReservationGridRowHeader-Inner')
avail = driver.find_elements_by_class_name('ReservationGridCell-Inner')

current_hour = strftime('%I')
print(current_hour)
current_minutes = strftime('%M')
print(current_minutes)
current_half = strftime('%p')

#format to 30min increments
if int(current_minutes) >= 30:
    current_time = current_hour + ':30 ' + current_half
else:
    current_time = current_hour + ':00 ' + current_half

print(current_time)
current_time = re.sub('^0', '', current_time)  #remove 0 on front of hour
print('current time in 30min incr is: ' + current_time)

for i in range(len(time)):
    print(str(i) + ' ' + time[i].text + ' ' + avail[i].text)
    if time[i].text == current_time:
        print('hours match')
        print(current_time)
        print('Next session: ' + time[i + 1].text)
        if avail[i + 1].text == 'Available':
            print('THERE IS NOBODY AT THE GYM')
            next_session = avail[i + 1]
            print('next session: ' + next_session.text)
            break

print('outside for: ' + next_session.text)
next_session.click()

check_box = driver.find_element_by_class_name('checkbox-label-wrap').click()

save = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div/div/div[2]/div/div/div/div[5]/div/div[1]/div/div/div[3]/table/tbody/tr/td[2]/div/div/a[2]/span').click()