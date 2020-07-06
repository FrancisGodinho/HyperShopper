from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

from browser.browser import Browser
from user.user import User

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

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button"))).click()
        except (TimeoutException, ElementClickInterceptedException):
            return False 

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/div[2]/div/div/div/div/div[3]/button[2]"))).click()
        except (TimeoutException, ElementClickInterceptedException):
            return False 
        

        return True
        
    def checkout(self, timeout=20):
        
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_FirstName\"]"))).send_keys(self.user.get_data("Name").split()[0]) #first name
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_LastName\"]"))).send_keys(self.user.get_data("Name").split()[1]) #last name
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_PostCode\"]"))).send_keys(self.user.get_data("Zip"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_Address1\"]"))).send_keys(self.user.get_data("Address"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_Address3\"]"))).send_keys(self.user.get_data("City"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_Territory\"]"))).send_keys(self.user.get_data("Province"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Shipping_phonenumber\"]"))).send_keys(self.user.get_data("Tel"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shipping_Email\"]"))).send_keys(self.user.get_data("Email"))

        #go to billing and payment
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"gdprSection\"]/div[1]/label[1]/span"))).click()
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"shippingSubmit\"]"))).click()
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"billingSubmit\"]"))).click()

        #card info

        #WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"CreditCardHolder\"]"))).click() #card name
        #WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"CreditCardHolder\"]"))).send_keys(self.user.get_data("Name")) #card name
        #WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"KKnr\"]"))).send_keys(self.user.get_data("Card Number"))
        #WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"KKMonth\"]"))).send_keys(self.user.get_data("Exp Date")[:3])
        #WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"KKYear\"]"))).send_keys("20" + self.user.get_data("Exp Date")[3:])
        #WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"CCCVC\"]"))).send_keys(self.user.get_data("CVV"))

        #purchase
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"BtnPurchase\"]"))).click()
        
        
        
