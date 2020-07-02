from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from user.user import User

class Browser:
    
    def __init__(self, user):
        self.user = user
        self.driver = None
    
    def launch(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def close(self):
        self.driver.quit()

    def add_to_cart(self, timeout=10):
        pass

    def add_to_cart_bylink(self, link, timeout=10):
        pass

    def checkout(self, timeout=10):
        pass

