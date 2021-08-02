from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import datetime

import sys
from ITennis.yokohama.yokohama_handler import YokohamaHandler

class EfficientTennisDriver():

    def __init__(self):
        pass

    def reserve(self):
        raise NotImplementedError

    def watch_and_reserve(self):
        raise NotImplementedError


class YokohamaTennisDriver(EfficientTennisDriver):

    def __init__(self, user_id_str, passwd_str):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.__driver = webdriver.Chrome(options=options)
        self.__driver.get('https://yoyaku.city.yokohama.lg.jp/')
        time.sleep(1)
        self.__handler = YokohamaHandler()
        self.__driver = self.__handler.login(self.__driver, user_id_str, passwd_str) 

    def reserve(self, place, date):
        # [NOTE]: RSGK001_05 is "空状況"
        available_courts = self.__driver.find_element(By.ID, 'RSGK001_05')
        available_courts.click()

        # [NOTE]: for sports
        button = self.__driver.find_element(By.ID, 'fbox_01') 
        button.click()

        # [NOTE]: for tennis courts
        button = self.__driver.find_element(By.ID, 'fbox_05') 
        button.click()

        # [NOTE]: place selection
        button = self.__handler.select_facility(self.__driver, place)
        button.click()

        button = self.__driver.find_element(By.ID, 'fbox_00') 
        button.click()

        # [NOTE]: date selection
        # [NOTE]: This is tentative process to go to August from July page.
        # goto_list = self.__driver.find_elements_by_class_name("goto")
        # goto_button = goto_list[-1].find_element_by_tag_name("button")
        # goto_button.click()

        button_id = "idbtn_{}".format(date.day) 
        button = self.__driver.find_element(By.ID, button_id) 
        button.click()

        start_time = (str(date.hour).zfill(2) + str(date.minute).zfill(2))
        # [NOTE]: Assuming 2 hours playing
        end_time = (str(date.hour+2).zfill(2) + str(date.minute).zfill(2))
        search_time = start_time + "-" + end_time

        while True:
            # now = datetime.datetime.now().strftime("%H:%M:%S")
            # if now == "07:00:00":
            # [NOTE]: tentative
            # reserve_start_time = datetime.datetime(2021, 7, 20, 7, 00, 00)

            # delta = reserve_start_time - datetime.datetime.now()
            # delta = datetime.datetime.now() - reserve_start_time
            # print("delta", delta.days)
            # if now:
            #     time.sleep(0.1)
            print(datetime.datetime.now())
            try:
                self.__handler.find_element_from_table(self.__driver, search_time)
            except RuntimeError:
                self.__handler.go_back_to_page(self.__driver)
                continue

            # [NOTE]: go to confirmation
            self.__handler.go_to_next_page(self.__driver)

            # [NOTE]: go to final confirmation 
            self.__handler.go_to_next_page(self.__driver)

            # [NOTE]: make a reservation
            self.__handler.go_to_next_page(self.__driver)
            break
            # else:
                # time.sleep(0.1)
