# coding=utf-8
import time,datetime

from selenium import webdriver

url="http://www.xhsd.com"
driver=webdriver.Chrome()
driver.get(url)

driver.maximize_window()
time.sleep(1)
driver.find_element_by_id('search-input').send_keys(u"福尔摩斯")
driver.find_element_by_id('js-search-site').click()
nowhandle=driver.current_window_handle
allhandles=driver.window_handles
for handle in allhandles:
    if handle !=nowhandle:
        driver.switch_to_window(handle)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div/div/div[4]/ul/li[1]/p[1]/a").click()
driver.get_screenshot_as_file("C:\ForJenkins\测试jenkins%s.png"% datetime.datetime.now().strftime('%Y%m%d.%H%M%S.%f')[:-3])
time.sleep(2)
driver.back()
time.sleep(3)
driver.quit()


