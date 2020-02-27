from django.test import LiveServerTestCase
from django.test import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.common.exceptions import WebDriverException


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):

        # self.browser = webdriver.Edge()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_page_update(self):
        time.sleep(1)
        MAX_WAIT = 16
        start_time = time.time()
        while True:
            try:
                header = self.browser.find_element_by_tag_name('html')
                return True
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    def test_user_can_checkout_page(self):
        self.browser.get(self.live_server_url+"/calculator")
        self.assertEqual("Calculator", self.browser.title)

    def test_user_can_calculate(self):
        self.browser.get(self.live_server_url+"/calculator")
        self.wait_for_page_update()

        x_input = self.browser.find_element_by_id("input_x")
        x_input.send_keys("5")
        op_input  =self.browser.find_element_by_id("input_op")
        op_input.send_keys("*")
        y_input = self.browser.find_element_by_id("input_y")
        y_input.send_keys("4")


        button = self.browser.find_element_by_id("enter")
        button.click()
        self.wait_for_page_update()

        result= self.browser.find_element_by_id("result").text
        self.assertEqual(20,float(result))
