import asyncio
import asyncio.subprocess

async def _run_command_async(command_list):
    command_name = command_list[0]
    try:
        process = await  asyncio.create_subprocess_exec(
            *command_list, 
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        await process.wait()
        
        if process.returncode ==0:
            return 'OK'
        else:
            return f"Failed (Exit code {process.returncode})"
    except FileNotFoundError:
        return f"Failed (Command not found: '{command_name}')"
    except Exception as e:
        return f"Failed (Unexpected error: {type(e).__name__})"
    
        
async def check_dns():
    return await _run_command_async(["getent", "hosts", "google.com"])
    
async def ping_test():
    return await _run_command_async(["ping", "-c", "1", "8.8.8.8"])
        
    
async def network_info():
    dns_status, ping_status = await asyncio.gather(
        check_dns(),
        ping_test(),
    )
    
    return {
        "dns": dns_status,
        "ping_google": ping_status,
    }
    
