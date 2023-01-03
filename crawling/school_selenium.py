from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
service = ChromeService(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


def craw():
    driver.get("https://sadang.sen.ms.kr")
    ul = driver.find_elements(By.CSS_SELECTOR, ".main_small_list")[0].find_elements(
        By.TAG_NAME, "li"
    )
    for li in ul:
        print(li.text)
    return


craw()
