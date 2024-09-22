import time
import selenium.webdriver.edge
import pytest
from selenium import webdriver
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    #driver = webdriver.Edge()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()
    print("hello")

    time.sleep(5)

    request.cls.driver = driver

    yield
    driver.close()



