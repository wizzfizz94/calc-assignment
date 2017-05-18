# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Path2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://teaching.csse.uwa.edu.au/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_path2(self):
        driver = self.driver
        driver.get(self.base_url + "/units/CITS5501/Assignments/calculator.html")
        driver.find_element_by_id("delete").click()
        driver.find_element_by_xpath("//button[@value='%']").click()
        driver.find_element_by_xpath("//button[@value='+']").click()
        driver.find_element_by_xpath("//button[@value='-']").click()
        driver.find_element_by_xpath("//button[@value='*']").click()
        driver.find_element_by_xpath("//button[@value='/']").click()
        driver.find_element_by_id("eqn-bg").click()
        driver.find_element_by_xpath("//button[@value='.']").click()
        driver.find_element_by_css_selector("div.rows > #delete").click()
        driver.find_element_by_xpath("//button[@value='1']").click()
        driver.find_element_by_xpath("//button[@value='2']").click()
        driver.find_element_by_xpath("//button[@value='3']").click()
        driver.find_element_by_xpath("//button[@value='6']").click()
        driver.find_element_by_xpath("//button[@value='5']").click()
        driver.find_element_by_xpath("//button[@value='4']").click()
        driver.find_element_by_xpath("//button[@value='7']").click()
        driver.find_element_by_xpath("//button[@value='8']").click()
        driver.find_element_by_xpath("//button[@value='9']").click()
    
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
