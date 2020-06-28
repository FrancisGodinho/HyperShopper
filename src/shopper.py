from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from browser.supreme_browser import SupremeBrowser
from user.user import User

user = User(shirt_size="Large") #set size
user.set_all_data({
        "name": "Francis Godinho",
        "email": "francisgodinho2010@gmail.com",
        "tel": "7781234567",
        "address": "12345 Test Street", 
        "country": "Canada",
        "state": "BC", 
        "zip": "V1A2B3",
        "city": "Richmond",
        "card_num": "1010101010101010",
        "card_month": "10",
        "card_year": "2021",
        "cvv": "123"
})

browser = SupremeBrowser(user)
browser.launch()
added = browser.add_to_cart_bylink("https://www.supremenewyork.com/shop/jackets/p7z6mv4ur/p5eiyuxlj")
if added:
        browser.checkout()
        
else:
        print("NO SIZE")

browser.close()
