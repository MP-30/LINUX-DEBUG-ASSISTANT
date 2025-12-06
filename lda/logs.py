import subprocess

def journal_errors():
    try:
        out = subprocess.check_output(["journalctl", "-p", "3", "-n", "50"], text=True)
        return out.split("\n"[-10:])
    except:
        return ["Could not read logs"]

    
    