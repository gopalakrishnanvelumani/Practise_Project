from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
from utilities.BaseClasss import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_1(self, setup, getData):
        # log = self.getLogger()
        homePage = HomePage(self.driver)

        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((homePage.getname()))
        )
        name_input.send_keys(getData["name"])

        # self.elementToBeClickable(homePage.getname().send_keys(getData["email"])


        # homePage.getname().send_keys(getData["name"])
        homePage.getemail().send_keys(getData["email"])
        self.selectOptionByText(homePage.getDropdown(), getData["gender"])
        self.driver.refresh()
        # log.info("Page is successfully tested")

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param






















        # self.driver.find_element(By.NAME, "name").send_keys("Gopalakrishnan Velumani")
        # self.driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
