import psutil

def top_process():
    processes = [(p.pid, 
                  p.info["cpu_percent"],
                  p.info["name"])
                 for p in psutil.process_iter(['cpu_percent', 'name'])
                ]
    top = max(processes, key=lambda x: x[1])
    return {"pid": top[0], "cpu": top[1], "name":top[2]}

