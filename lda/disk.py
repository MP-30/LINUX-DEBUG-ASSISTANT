import psutil

def disk_info():
    disk = psutil.disk_usage('/')
    
    return {
        "total_gb": round(disk.total / 1e9, 2),
        "used_percent": disk.percent,
    }