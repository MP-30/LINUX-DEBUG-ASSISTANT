import psutil
from aiopsutil import AsyncPSUtil

async def disk_info():
    aps = AsyncPSUtil()
    # disk = await aps.disk_usage('/')
    disk = psutil.disk_usage('/')
    
    return {
        "total_gb": round(disk.total / 1e9, 2),
        "used_percent": disk.percent,
    }