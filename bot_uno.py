#!/usr/bin/env python

import unittest
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from time import sleep


class BotUno(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        main_driver = self.driver
        main_window = driver.current_window_handle
        return_driver = self.driver
        driver.get("http://recetas25.blogspot.com.es/2017/03/ella-perdio-7-kilos-en-10-dias-con-esta.html")
        driver.implicitly_wait(10)
        i = 1

        while True:
            i += 1
            try: driver.find_element_by_xpath("//ins[@class='adsbygoogle']").click()
            except NoSuchElementException as e: driver.quit()
            body = driver.find_element_by_tag_name("body")
            body.send_keys(Keys.LEFT_CONTROL + Keys.ENTER)
            ActionChains(driver).send_keys(Keys.LEFT_CONTROL + Keys.TAB).perform()
            sleep(10)
            ActionChains(main_driver).send_keys(Keys.LEFT_CONTROL + Keys.SHIFT + Keys.TAB).perform()
            driver.get("http://recetas25.blogspot.com.es/2017/03/ella-perdio-7-kilos-en-10-dias-con-esta.html")

            if i == 10:
                driver.close()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

