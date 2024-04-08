#pytest will come come here and check for fixtures added

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def login():
    pass
@pytest.fixture(scope="session")
def get_credentials_value():
    pass

#below we create fixture to open browser
@pytest.fixture()
def driver(login, get_credentials_value):
    chrome_options = Options()
    # chrome_options.page_load_strategy = 'normal' #under this value we don't wait until the full loading of the page
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--window-size=1500,900")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--disable cache")
    page = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    page.get("url")
    value = get_credentials_value()
    name = value["name"]
    password = value["password"]
    page.find_element("asdf").send_keys(name)
    page.find_element("fdg").send_keys(password)
    page.find_element("afgsdg").click()
    yield page
    page.quit() #this row will run after yield in previuos line. but if instead of yield there was return then
                  # driver.quit() would never run and browser would not be closed
