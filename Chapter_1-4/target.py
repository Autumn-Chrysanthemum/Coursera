# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

chromedriver = "/Users/u449/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

class Target(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www-secure.target.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_target(self):
        driver = self.driver
        driver.get(self.base_url + "/giftcard/check-balance")
        try: self.assertEqual("check a GiftCard balance", driver.find_element_by_css_selector("h1.title-text.alpha").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("cardNumber").clear()
        driver.find_element_by_id("cardNumber").send_keys("041-300-967-839-981")
        driver.find_element_by_id("cardAccessCode").clear()
        driver.find_element_by_id("cardAccessCode").send_keys("95070220")
        driver.find_element_by_id("checkBalance").click()
        try: self.assertEqual("check a GiftCard balance", driver.find_element_by_css_selector("h1.title-text.alpha").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        value = driver.find_element_by_css_selector("p.h-zeroMargin > strong").text
        CARD = driver.find_element_by_xpath("//div[@id='gcBalanceMainContainer']/div/div/div[2]/div/span[2]").text
        ACCESS = driver.find_element_by_css_selector("p.h-zeroMarginBottom").text
        print(value)
        print(CARD)
        print(ACCESS)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
