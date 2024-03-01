from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    dropdown = (By.ID, "exampleFormControlSelect1")

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)
