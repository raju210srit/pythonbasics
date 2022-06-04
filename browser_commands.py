    from selenium import webdriver
    time.sleep()
    driver=webdriver.Chrome (r"C:\Users\User\PycharmProjects\QESB2\Drivers\chromedriver.exe")
    url=r"https://pyspiders.com/"
    driver.get(url)
    time.sleep(4)
    driver.maximize_window()
    time.sleep(2)
    url=r"https://facebook.com"
    driver.get(url)
    time.sleep(4)
    driver.back()
    time.sleep(3)
    driver.farward()
    driver.close()
C:\Users\User\PycharmProjects\QESB2


