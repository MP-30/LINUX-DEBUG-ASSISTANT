from .cpu import cpu_info
from .memory import memory_info
from .disk import disk_info
from .network import network_info
from .processes import top_processes
from .docker_stats import docker_info
from .logs import journal_errors

async def full_summary():
    return{
        "cpu": await cpu_info(),
        "memory": await memory_info(),
        "disk": await disk_info(),
        "network": await network_info(),
        "top_process": await top_processes(3),
        "docker": await docker_info(),
        "errors": await journal_errors()
    }
    
