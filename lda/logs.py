import asyncio
import asyncio.subprocess
from lda.commands import Commands


async def journal_errors():
    try:
        process = await asyncio.create_subprocess_exec(
            *Commands.JOURNAL_ERRORS,
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
        

    
    