from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException



from browser.browser import Browser
from user.user import User

from time import sleep


class NikeBrowser(Browser):


    def add_to_cart_bylink(self, link, timeout=20):
        self.driver.get(link)

        found_size = False
        for i in range(1, 17):
            if len(self.driver.find_elements_by_xpath(f"//*[@id=\"root\"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[{i}]")) != 0:
                if WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, f"//*[@id=\"root\"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[{i}]/button"))).get_attribute('innerHTML') == 'US ' + str(self.user.shoe_size()):
                    WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, f"//*[@id=\"root\"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[{i}]/button"))).click()
                    found_size = True
                    break
        
        if not found_size:
            return False
        

        sleep(1)

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button"))).click()
        except (TimeoutException, ElementClickInterceptedException):
            return False 

        sleep(1)

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/div[2]/div/div/div/div/div[3]/button[2]"))).click()
        except (TimeoutException, ElementClickInterceptedException):
            return False 
        

        return True
        
    def checkout(self, timeout=20):
        
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_FirstName\"]"))).send_keys(self.user.get_data("Name"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_LastName\"]"))).send_keys(self.user.get_data("Name"))
