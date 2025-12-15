import asyncio

async def journal_errors():
    try:
        process = await asyncio.create_subprocess_exec(
            "journalctl", 
            "-p", 
            "3", 
            "-n" , 
            "50",
            "--no-pager",
            stdout=asyncio.subprocess.PIPE, 
            stderr=asyncio.subprocess.PIPE, 
        )
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
            error_message = stderr.decode().strip()
            return [f"Could not read logs: Subprocess failed. Error: {error_message[:100]}..."]

        output = stdout.decode().strip()
        lines = output.split('\n')
        
        return lines[-10:]
    
    except FileNotFoundError:
        return ["Could not read logs: 'journalctl' command not found"]
    
    except Exception as e:
        return [f"Could not read logs: Unexcepteed internal error: {e}"]        
        

    
    