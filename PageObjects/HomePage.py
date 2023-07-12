from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    shop=(By.XPATH,"//a[@href='/protocommerce/shop']")
    name=(By.CSS_SELECTOR,"[name='name']")
    email=(By.NAME,"email")
    password=(By.XPATH,"//input[@id='exampleInputPassword1']")
    gndr=(By.ID,"exampleFormControlSelect1")
    status=(By.XPATH,"//input[@id='inlineRadio2']")
    gtdate=(By.XPATH,"//input[@type='date']")
    sbmt=(By.XPATH,"//input[@value='Submit']")
    alrtmsg=(By.CSS_SELECTOR,"[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(HomePage.shop).click()
        checkoutpg=CheckOutPage(self.driver)
        return checkoutpg

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def enterpwd(self):
        return self.driver.find_element(*HomePage.password)

    def selectgndr(self):
        return  self.driver.find_element(*HomePage.gndr)
    def getstatus(self):
        return self.driver.find_element(*HomePage.status)
    def getdate(self):
        return self.driver.find_element(*HomePage.gtdate)
    def submt(self):
        return self.driver.find_element(*HomePage.sbmt)
    def alrt(self):
        return self.driver.find_element(*HomePage.alrtmsg)





