from .cpu import cpu_info
from .memory import memory_info
from .disk import disk_info
from .network import network_info
from .processes import top_processes
from .docker_stats import docker_info
from .logs import journal_errors as old_journal_errors
from .logs_new import classify_log,extract_actionable_issues

async def full_summary():
    raw_logs = await old_journal_errors()
    actionable_logs, ignored_logs = classify_log(raw_logs)
    issues = extract_actionable_issues(actionable_logs)
    count = len(ignored_logs['Non_actionable']) + len(ignored_logs['Not_matched'])
    return{
        "cpu": await cpu_info(),
        "memory": await memory_info(),
        "disk": await disk_info(),
        "network": await network_info(),
        "top_process": await top_processes(3),
        "docker": await docker_info(),
        # "errors": await journal_errors(),
        "health": "degraded" if issues else "healthy",
        "actionable_issues": issues,
        "ignored_error_count": count,
        "ignored_error": ignored_logs
    }