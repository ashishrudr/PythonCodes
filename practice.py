from selenium import webdriver

driver=webdriver.Chrome("C:/Users/rudra/PycharmProjects/pythonProject1/chromedriver/chromedriver.exe")
driver.get("http://biharbhumi.bihar.gov.in/Biharbhumi/")
driver.find_element(By.XPATH, '//span[text()="जमाबंदी पंजी देखें"]').click()
