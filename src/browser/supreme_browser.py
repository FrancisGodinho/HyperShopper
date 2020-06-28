from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from browser.browser import Browser
from user.user import User

class SupremeBrowser(Browser):
    
    def add_to_cart(self, sub_cat, item_id, timeout=10):
        self.driver.get(f"https://www.supremenewyork.com/shop/{sub_cat}/{item_id}")
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, ' //*[@id="add-remove-buttons"]/input'))).click()
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cart"]/a[2]'))).click()
    
    def add_to_cart_bylink(self, link, timeout=10):
        self.driver.get(link)

        user_size = self.user.shirt_size()
        if "pants" in link or "shorts" in link:
            user_size = self.user.pant_size()
        if "shoes" in link:
            user_size = self.user.shoe_size()

        # Check if this item has sizes and select the appropriate size 
        try:
            if self.driver.find_element_by_xpath('//*[@id="s"]').get_attribute("aria-labelledby") is not None:
                if user_size.upper() not in WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="s"]'))).get_attribute('innerHTML').upper():
                    return False

                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="s"]'))).send_keys(user_size)
        except NoSuchElementException:
            pass
        
        # Add item to cart if possible
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, ' //*[@id="add-remove-buttons"]/input'))).click()
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cart"]/a[2]'))).click()
        except TimeoutException:
            return False

        return True

    def checkout(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_billing_name"]'))).send_keys(self.user.get_data("name"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_email"]'))).send_keys(self.user.get_data("email"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_tel"]'))).send_keys(self.user.get_data("tel"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bo"]'))).send_keys(self.user.get_data("address"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_billing_country"]'))).send_keys(self.user.get_data("country"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_billing_zip"]'))).send_keys(self.user.get_data("zip"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_billing_city"]'))).send_keys(self.user.get_data("city"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="order_billing_state"]'))).send_keys(self.user.get_data("state"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rnsnckrn"]'))).send_keys(self.user.get_data("card_num"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="credit_card_month"]'))).send_keys(self.user.get_data("card_month"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="credit_card_year"]'))).send_keys(self.user.get_data("card_year"))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="orcer"]'))).send_keys(self.user.get_data("cvv"))

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cart-cc"]/fieldset/p[2]/label/div'))).click()
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pay"]/input'))).click()

