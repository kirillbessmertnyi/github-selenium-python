import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#Set some selenium chrome options - Optional
#These options set your driver to run headless or not.
chrome_Options = Options()
chrome_Options.add_argument('--headless')

#Initialize your Chrome Driver with services and options (optional)
#For mor info on running headless, there's a link below in description
driver = webdriver.Chrome(options=chrome_Options)


# This you have to run the driver here. Your execution will depend.
AQUA_TC_ID = '270'
def test_initialize_browser():
    driver.get("https://Google.com")
    print("starting_Driver")
    content = driver.find_element(By.CLASS_NAME, "gLFyf")
    content.click()
    content.send_keys("The Text")
    content.send_keys(Keys.RETURN)
    result_stats = driver.find_element(By.ID, "result-stats")
    assert result_stats.is_displayed
    print(result_stats.text)
