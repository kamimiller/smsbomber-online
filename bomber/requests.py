import aiohttp,asyncio

async def getRequest(url,data):
    
    async with aiohttp.ClientSession() as session:
        
        async with session.get(url) as response:return response
            
async def postRequest(url,data):
    
    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:return response