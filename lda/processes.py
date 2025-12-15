import psutil
import asyncio


def _get_top_processes(limit=3):
    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            cpu = p.info['cpu_percent']
            if cpu > 0:
                processes.append(
                    {"pid": p.pid, "cpu": cpu, "name": p.info["name"]}
                )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort descending by CPU usage
    processes.sort(key=lambda x: x["cpu"], reverse=True)

    return processes[:limit]


async def top_processes(limit=3):
    """
    Returns top N CPU-consuming processes (async-safe)
    """
    # Initialize CPU counters
    psutil.cpu_percent(interval=None)
    for p in psutil.process_iter():
        p.cpu_percent(interval=None)

    # Sampling window
    await asyncio.sleep(0.5)

    return await asyncio.to_thread(_get_top_processes, limit)
