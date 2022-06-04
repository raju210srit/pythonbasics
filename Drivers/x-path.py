from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\User\PycharmProjects\QESB2\Drivers\chromedriver.exe")
#url=r"https://opensource-demo.orangehrmlive.com/"
# url=r"http://demowebshop.tricentis.com/"
driver.get(r"http://demowebshop.tricentis.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//input[@id='txtusername']").send_keys("admin")
driver.find_element(By.XPATH,"//a[text()='Log in']").click()
driver.find_element(By.XPATH,"//input[contains(@class,'email')]").send_keys("ka")
driver.find_element(By.XPATH,"//input[contains(@type,'word')]").send_keys("123")
time.sleep(3)
driver.find_element(By.XPATH,"//label[contains(text(),'Rem')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Forgot password?')]").click()


