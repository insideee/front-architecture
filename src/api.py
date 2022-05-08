import asyncio
from PySide6.QtCore import QThread, Signal
import aiohttp
import constants


async def fetch(session, base_url, endpoint, params, headers, data, json, method) -> dict:
    try:
        if method == 'GET':
            async with session.get(f'{base_url}{endpoint}', headers=headers, params=params, data=data, json=json) as response:
                data = await response.json()

                if type(data) == list:
                    return {'status_code': response.status,
                            'data': data}
                
                return {'status_code': response.status,
                        **data}
                
        elif method == 'POST':
            async with session.post(f'{base_url}{endpoint}', headers=headers, params=params, data=data, json=json) as response:
                data = await response.json()
                
                return {'status_code': response.status,
                        **data}
                
        elif method == 'PUT':
            async with session.put(f'{base_url}{endpoint}', headers=headers, params=params, data=data, json=json) as response:
                data = await response.json()
                
                return {'status_code': response.status,
                        **data}
                
        elif method == 'DELETE':
            async with session.delete(f'{base_url}{endpoint}', headers=headers) as response:
                data = await response.json()
                
                return {'status_code': response.status,
                        **data}
            
    except Exception as e:
        print('error', e)
        return {'status_code': 500,
               'detail': 'Unable to connect. Try again'}


async def make_request(*args):
    timeout = aiohttp.ClientTimeout(total=10)
    url = constants.API_URL

    async with aiohttp.ClientSession(timeout=timeout) as session:
        task = [fetch(session=session, base_url=url, **args[i])
                for i in range(len(args))]
        
        return await asyncio.gather(*task)


class RequestThread(QThread):
    
    data = Signal(list)
    
    def __init__(self, *args):
        super(RequestThread, self).__init__()
        self.request = args
        
    def run(self):
        data =  asyncio.run(make_request(*self.request))
        self.data.emit(data)