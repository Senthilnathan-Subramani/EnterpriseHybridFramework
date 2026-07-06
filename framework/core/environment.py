import os
class Environment:
    @staticmethod
    def get(name:str, default:str=''):
        return os.getenv(name, default)
