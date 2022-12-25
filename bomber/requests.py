import aiohttp,asyncio
import requests as req

def getRequest(url):
    
    with req.Session() as session:
        
        with session.get(url) as response:return response
            
def postRequest(url,data):
    
    with req.Session() as session:

        with session.post(url, data=data) as response:return response