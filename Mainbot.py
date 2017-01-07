import argparse, os, time
import urlparse, random
from selenium import webdriver
driver = webdriver.Chrome()

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def ClickTime(browser):
    while True:
        time.sleep(random.uniform(3.5, 6.9))

        clickElement = browser.find_element_by_class_name("primary")
        clickElement.click()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="tagged email")
    parser.add_argument("password", help="tagged password")
    args = parser.parse_args()

    browser = webdriver.Chrome()
    browser.get("https://secure.tagged.com/register.html?display=login")
    browser.switch_to_frame("unified_login")

    emailElement = browser.find_element_by_id("username_login")
    emailElement.send_keys(args.email)
    passElement = browser.find_element_by_id("password_login")
    passElement.send_keys(args.password)
    passElement.submit()

    os.system('cls')
    print "[+] Success Logged in"
    browser.get("http://www.tagged.com/meetme")
    ClickTime(browser)








if __name__ == "__main__":
    Main()
