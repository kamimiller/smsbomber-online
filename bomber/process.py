from secrets import token_hex
from multiprocessing import Process,cpu_count
from concurrent.futures import ProcessPoolExecutor
from bomber.requests import postRequest,getRequest
from sms_bomber.models import Bomber
                        
def startBomber(task_id):
    Bomber.process.get(task_id)["process"].start()
    Bomber.process.get(task_id)["status"] = "starting"

def stopBomber(task_id):
    Bomber.process[task_id]["process"].terminate()
    del Bomber.process[task_id]

def createBomber(target):
    task_id = token_hex(16)
    Bomber.process[task_id] = {
        "status" : "padding",
        "process" : Bomber(target,task_id),
        "target" : target
    }
    return Bomber.process.get(task_id)["process"]