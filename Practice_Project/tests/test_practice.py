import time
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.PracticePage import PracticePage
from utilities.BaseClasss import BaseClass


class TestPractice(BaseClass):

    def test_practice(self,setup):
        log = self.getLogger()
        practice = PracticePage(self.driver)
        practice.getCheckBox().click()  #CheckBox

        # radioButtons = practice.getRadioButton()
        # radioButtons[2].click()

        radioButtons = self.driver.find_elements(By.NAME, "radioButton")
        radioButtons[2].click()


        self.selectOptionByText(practice.getDropdown(), "Option3")



        # dropdown = Select(practice.getDropdown())
        # dropdown.select_by_visible_text("Option3")





        self.driver.find_element(By.ID, "autocomplete").send_keys("ind")
        countries = self.driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
        for country in countries:
            if country.text == "India":
                country.click()
                break

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, "mousehover")).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
        # log.info("Product is tested successfully")



        # time.sleep(5)



















        # self.driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#checkBoxOption2").click()





        # checkboxes = self.driver.find_elements(By.ID, "//input[@type='checkbox']")
        # for checkbox in checkboxes:
        #     if checkbox.get_attribute("value") == "option3":
        #         checkbox.click()
        #         assert checkbox.is_selected()
        #         break