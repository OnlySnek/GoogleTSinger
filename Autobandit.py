from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.google.com/")

searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
titel = str("Sexy bitch")
kunstner = str("David Guetta lyrics")
searchbox.send_keys(titel + " " + kunstner + (Keys.ENTER))

linkButton = driver.find_element_by_class_name('hide-focus-ring.pSO8Ic.vk_arc')
linkButton.click() 

time.sleep(2)

kopierBandit = driver.find_elements_by_class_name("bbVIQb")


Tekst = kopierBandit[0].text + '\n' + kopierBandit[1].text

translateside = driver.find_element_by_class_name('gLFyf.gsfi')
translateside.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
translateside.send_keys(Keys.DELETE)
time.sleep(1)

translateside.send_keys("google translate" + (Keys.ENTER))

finddansk1 = driver.find_element_by_xpath('//*[@id="tw-tl"]')
finddansk1.click()

finddansk2 = driver.find_element_by_xpath('//*[@id="tl_list-search-box"]')

finddansk2.send_keys("da" + (Keys.ENTER))


translater = driver.find_element_by_xpath('//*[@id="tw-source-text-ta"]')

translater.send_keys(Tekst)
time.sleep(1)
translaterlyd = driver.find_element_by_xpath('//*[@id="tw-spkr-button"]/span')
translaterlyd.click()






