import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.PracticePage import PracticePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(messsage)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def elementToBeClickable(self, text):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, text))
        )



    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)



    # logger.debug("A debug statement is executed")
    # logger.info("Information statement")
    # logger.warning("Something is in warning mode")
    # logger.error("A major error has happened")
    # logger.critical("Critical issue")


    # logging.basicConfig(filename= "D:\Krishna_Testing\Log\testing.log",
    #                     filemode= 'w',)
    # log = logging.getLogger()
    # log.setLevel((logging.DEBUG))
    # log.debug("This is debug log")
    # log.info("This is info log")
    # log.error("This is error log")
    # log.warning("This is warning log")
    # log.critical("This is critical log")


