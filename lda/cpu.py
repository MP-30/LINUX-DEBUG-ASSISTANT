import psutil
from aiopsutil import AsyncPSUtil

async def cpu_info():
    aps = AsyncPSUtil()
    return {
        "usage_percent": await aps.cpu_percent(interval=1),
        "core_count": psutil.cpu_count(),
        "load_avg": await aps.getloadavg()
    }
    