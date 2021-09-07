from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://accstorefront.csz8zfle01-shoaltert1-d1-public.model-t.cc.commerce.ondemand.com/zh/")
driver.maximize_window()
time.sleep(2)


def pagetest():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btnCloseLarge")))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "bannerTopCloseButton")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[2]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[3]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[4]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[5]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[6]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[7]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[8]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[9]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[10]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[11]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[12]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[13]/a")))
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/ul/li[14]/a")))
    element.click()
    driver.switch_to.alert.accept()


pagetest()