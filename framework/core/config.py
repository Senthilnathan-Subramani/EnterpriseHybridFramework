from dotenv import load_dotenv
load_dotenv()
from .environment import Environment
class Config:
    browser=Environment.get('BROWSER','chrome')
    base_url=Environment.get('BASE_URL','https://example.com')
