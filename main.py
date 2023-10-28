print("\t\033[1;32m COIN GENERATOR \033[1;36m Latest \n\n")
import time
from aminofix import Client 
from aminofix import SubClient
from aminofix.lib.util.exceptions import * 
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import path
import json
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"acc.json")
dictlist=[]
cid="140130420" # community id here's

with open(emailfile) as f: 
    dictlist = json.load(f) 

def magicnum(): 
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime 

def sendobj(sub : SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ] 
    sub.send_active_obj(timers=timer,
tz=-60) 

def log(cli : Client,email : str, password : str):
    try:  
        cli.login(email=email,password=password)
        print(f"logged into {email}\n")
    except VerificationRequired:
        print(f"Verification required for {email}")
    except InvalidPassword or InvalidAccountOrPassword:
        print(f"Incorrect password for {email}")
    except: 
        print(f"An unkown error has occoured for {email}")
        pass # Passes 

def task(sub : SubClient,email : str,i : int):
    try: 
        sendobj(sub) 
        print(f"Sent coin generating object for {email} times :- {i+1}")
    except:
        return None

def threadit(acc : dict):
    email=acc["email"]
    device=acc["device"]
    password=acc["password"]
    client=Client(deviceId=device)
    log(cli=client,email=email,password=password)
    client.join_community(cid)
    subclient=SubClient(comId=cid,profile=client.profile)
    print("Done")
    with ThreadPoolExecutor(max_workers=1) as executorx:
        _ = [executorx.submit(task, subclient,email,i)for i in range(25)]
    client.logout()
    time.sleep(25)
    print(f"FINISHED MINING {email}")

def main():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
    	threadit(amp)
    print("Mining with all accounts finished")
 
if __name__ == '__main__': 
    main()
