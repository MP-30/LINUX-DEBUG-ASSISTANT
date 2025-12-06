import psutil

def memory_info():
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total /1e9, 2),
        "used_percent": mem.percent,
    }