from bomber import requests
from asyncio import run

if __name__ == '__main__':
    run(requests.getRequest("https://google.com"))