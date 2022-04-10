import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path=r"C:\Users\Benas\Desktop\webdriver\msedgedriver.exe")
driver.maximize_window()
#enter to youtube
driver.get("https://www.youtube.com/")
time.sleep(3)
#send in search box "tell me.."
driver.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys('tell me why brooklyn 99')
#click on search
driver.find_element(by=By.XPATH,value='//*[@id="search-icon-legacy"]').click()
time.sleep(3)
#click on video
driver.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
time.sleep(3)
#like
driver.find_element(by=By.XPATH,value='//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]/a').click()
time.sleep(10)
driver.close()
