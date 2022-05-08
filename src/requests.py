import api 
from PySide6.QtCore import QThread


def login_request(username:str, password: str) -> dict:
    return {'endpoint': '/login',
            'headers': None,
            'params': None,
            'data': {'username': username,
                     'password': password},
            'json': None,
            'method': 'POST'}
    
    
def make_request(connect_to, *args) -> QThread:
    request_thread = api.RequestThread(*args)
    request_thread.start()
    request_thread.data.connect(connect_to)
    return request_thread