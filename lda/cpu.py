import psutil

def cpu_info():
    return {
        "usage_percent": psutil.cpu_percent(interval=1),
        "core_count": psutil.cpu_count(),
        "load_avg": psutil.getloadavg()
    }
    