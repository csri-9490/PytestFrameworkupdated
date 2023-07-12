from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver=driver

    cardTitles=(By.XPATH, "//div[@class='card h-100']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    cardFooter=(By.XPATH,"div/button")
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    checkout=(By.CSS_SELECTOR, "a[class*='btn-primary']")
    def getCheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    checkout2=(By.XPATH, "//button[@class='btn btn-success']")
    def getCheckout2(self):
        # return self.driver.find_element(*CheckOutPage.checkout)
       self.driver.find_element(*CheckOutPage.checkout).click()
       ConfirmPg=ConfirmPage(self.driver)
       return  ConfirmPg







