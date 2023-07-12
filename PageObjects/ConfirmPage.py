from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    loc=(By.ID, "country")
    locSel=(By.LINK_TEXT, "India")
    locclk=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    sbmit=(By.CSS_SELECTOR, "[type='submit']")
    alrt=(By.CLASS_NAME, "alert-success")

    def delloc(self):
        return self.driver.find_element(*ConfirmPage.loc)

    def dellocSel(self):
        return  self.driver.find_element(*ConfirmPage.locSel)


