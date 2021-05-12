# RUN startflask.py ON A SEPERATE TERMINAL BEFORE RUNNING THIS
  
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def main():
    # GET PATH ON ChromeDriverServer
    dir = os.path.dirname(__file__)
    chrome_driver_path = dir + "\chromedriver.exe"

    # CREATE A NEW SESSION
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # NAVIGATE TO REGISTER PAGE
    driver.get("http://127.0.0.1:5000/register")

    # ENTER USER DETAILS AND REGISTER
    search_field = driver.find_element_by_name("username")
    search_field.send_keys("1234")
    search_field = driver.find_element_by_name("email")
    search_field.send_keys("1234@gmail.com")
    search_field = driver.find_element_by_name("password")
    search_field.send_keys("123456")
    search_field = driver.find_element_by_name("password2")
    search_field.send_keys("123456")

    search_field = driver.find_element_by_name("submit").click()
    print("Register user........ok")


    # NAVIGATE TO LOGIN PAGE
    driver.get("http://127.0.0.1:5000/login")

    # ENTER USERNAME DETAILS AND SUBMIT
    search_field = driver.find_element_by_name("username")
    search_field.send_keys("1234")
    search_field = driver.find_element_by_name("password")
    search_field.send_keys("123456")

    search_field = driver.find_element_by_name("submit").click()
    print("Login user........ok")


    # GO THROUGH EVERYPAGE AND RUN THE QUIZZES
    pagelist = ["http://127.0.0.1:5000/lesson/1","http://127.0.0.1:5000/lesson/2","http://127.0.0.1:5000/lesson/3","http://127.0.0.1:5000/lesson/4","http://127.0.0.1:5000/lesson/5"]
    for page in pagelist:
        driver.get(page)

        driver.find_element_by_id("next-button").click()
        driver.find_element_by_id("next-button").click()

        alert_obj = driver.switch_to.alert
        alert_obj.accept()

        driver.find_element_by_id("answer-1").click()
        driver.find_element_by_id("answer-6").click()
        driver.find_element_by_id("answer-11").click()

        driver.find_element_by_id("submit-button").click()
        print(page+"........ok")

    # LOGOUT USER
    driver.get("/logout")
    print("Logout user........ok")

    # CLOSE BROWSER WINDOW WHEN COMPLETE
    driver.quit()   

    
main()


