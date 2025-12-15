import psutil
from aiopsutil import AsyncPSUtil

async def memory_info():
    aps = AsyncPSUtil()
    mem = await aps.virtual_memory()
    sw_mem = await aps.swap_memory()
    return  {
        "total_ram_gb": round(mem['total'] /1e9, 2),
        "used_percent_ram": mem['percent'],
        "total_swap_gb": round(sw_mem['total'] /1e9, 2),
        "used_percent_swap": sw_mem['percent']
    }