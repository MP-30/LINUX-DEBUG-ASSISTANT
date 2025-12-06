from .cpu import cpu_info
from .memory import memory_info
from .disk import disk_info
from .network import network_info
from .processes import top_process
from .docker_stats import docker_info
from .logs import journal_errors

def full_summary():
    return{
        "cpu": cpu_info(),
        "memory": memory_info(),
        "disk": disk_info(),
        "network": network_info(),
        "top_process": top_process(),
        "docker": docker_info(),
        "errors": journal_errors()
    }
    
