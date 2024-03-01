from selenium.webdriver.common.by import By

class PracticePage():

    def __init__(self, driver):
        self.driver = driver

    dropdown = (By.ID, "dropdown-class-example")
    checkBox1 = (By.CSS_SELECTOR, "#checkBoxOption1")
    radioButton = (By.NAME, "radioButton")


    def getCheckBox(self):
        return self.driver.find_element(*PracticePage.checkBox1)

    def getRadioButton(self):
        return self.driver.find_element(*PracticePage.radioButton)

    def getDropdown(self):
        return self.driver.find_element(*PracticePage.dropdown)





