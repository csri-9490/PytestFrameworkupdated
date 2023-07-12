import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self,text):
     element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionByText(self,locator,text):
        sel=Select(locator)
        sel.select_by_visible_text(text)

