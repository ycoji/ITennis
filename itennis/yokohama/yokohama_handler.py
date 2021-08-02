import time
from selenium.webdriver.common.by import By
from ITennis.yokohama.utils import get_button_id_from_court_name

class YokohamaHandler():

    def __init__(self):
        pass

    def login(self, driver, user_id_str, passwd_str):
        user_id = driver.find_element_by_name('ID')
        user_id.send_keys(user_id_str)
        password = driver.find_element_by_name('PWD')
        password.send_keys(passwd_str)
        login_button = driver.find_element_by_id('navi_login_r')
        login_button.click()
        time.sleep(1)
        print(driver.current_url)
        return driver

    def find_element_from_table(self, driver, search_time):
        print("find_element_from_table called.")
        table = driver.find_element_by_id("tbl_time")
        rows = table.find_elements(By.TAG_NAME, "tr")
        columns = [entry.text for entry in rows[0].find_elements(By.TAG_NAME, "th")]
        time_idx = columns.index(search_time)

        for row in rows[1:]:
            elements = row.find_elements(By.TAG_NAME, "td") 
            buttons = elements[time_idx].find_elements(By.TAG_NAME, "input")
            if buttons:
                buttons[0].click()

                error_messages = driver.find_elements_by_class_name("txt_error_message")
                if error_messages:
                    error = [e.text for e in error_messages]
                    raise RuntimeError("".join(error))

                else:
                    return

    def select_facility(self, driver, place):
        button_id = get_button_id_from_court_name(place) 
        while True:
            buttons = driver.find_elements_by_id(button_id)
            if buttons:
                return buttons[0]
            else:
                self.__go_to_next_tab(driver)

    def go_to_next_page(self, driver):
        # next_div = driver.find_elements_by_class_name("next")
        # next_div = driver.find_element_by_xpath("//div[last()]")
        # print(next_div)
        # next_button = next_div.find_element_by_tag_name("input")
        # next_button.click()
        # next_buttons = driver.find_elements_by_tag_name("input")
        # next_button = driver.find_element_by_xpath("//button[last()]")
        next_div = driver.find_element_by_id("footer")
        next_button = next_div.find_element_by_tag_name("button")
        next_button.click()

    def go_back_to_page(self, driver):
        back_div = driver.find_element_by_id("back_btn")
        back_button = back_div.find_element_by_tag_name("button")
        back_button.click()

    def __go_to_next_tab(self, driver):
        nexts = driver.find_elements_by_class_name("next")
        next_button = nexts[0].find_element_by_tag_name("button")
        next_button.click()
