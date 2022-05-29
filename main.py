from selenium import webdriver

driver = webdriver.Chrom('./chromedriver.exe')
driver.get('https://emeraldcity2residents.buildinglink.com/v2/tenant/amenities/availabilitygrid.aspx')

time = driver.find_elements_by_class_name('ReservationGridRowHeader-Inner')
avail = driver.find_elements_by_class_name('ReservationGridCell-Inner')

for i in range(len(time)):
    print(str(i) + ' ' + time[i].text + ' ' + avail[i].text)