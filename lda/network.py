import subprocess

def check_dns():
    try:
        subprocess.check_output(["systemmd-resolve", "--status"])
        return "OK"
    except:
        return "Failed"
    
def ping_test():
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return "OK"
        
    except: return "Failed"
    
def network_info():
    return {"dns": check_dns(),
            "ping_google": ping_test()    
        }
    
