"""
Smoke test
"""
import pytest
from selenium.webdriver.common.by import By


url = "https://testqastudio.me/"

def test_product_view_sku(browser):
    """
    Test case WERT-1
    """

    browser.get(url=url)
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()

    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11345"]')
    element.click()

    sku = browser.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'J4W5ADY72', "Unexpected sku"

@pytest.mark.smoke
def test_smoke(browser):
    """
    Test case SMK-1
    """
    browser.get(url=url)
    assert browser.current_url == url, ''
