import docker

def docker_info():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        return {"running_containers": len(containers)}
    except:
        return {"docker": "not running"}
