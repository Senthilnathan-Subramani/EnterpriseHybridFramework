from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .browser_options import chrome_options
from framework.core.config import Config
class DriverFactory:
    @staticmethod
    def create(headless=False):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options(headless))
