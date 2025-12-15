import docker
import asyncio


def _get_docker_data():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        if len(containers) > 0:
            return {
                "running_containers" : len(containers),
                "status": "running",
            }
        elif len(containers) == 0:
            return {
                "running_containers" : len(containers),
                "status": "0 conrainers running",
            }
    except Exception:
        return {
            "running_containers": 0,
            "status": "not running"
        }

async def docker_info():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _get_docker_data)