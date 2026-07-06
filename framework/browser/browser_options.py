from selenium.webdriver import ChromeOptions

def chrome_options(headless=False):
    o=ChromeOptions();
    o.add_argument('--headless=new') if headless else None
    o.add_argument('--start-maximized')
    return o
