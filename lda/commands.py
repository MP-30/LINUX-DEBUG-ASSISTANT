# network.py

class Commands:
    DNS_GOOGLE = ["getent", "hosts", "google.com"]
    PING_GOOGLE = ["ping", "-c", "1", "8.8.8.8"]
    JOURNAL_ERRORS = ("journalctl", "-p","3","-n","50", "--no-pager")
    
class ActionableKeywords:
    ACTIONABLE_PATTERNS = {
    "permission": ["Permission denied"],
    "dns": ["Host not found", "Temporary failure in name resolution"],
    "service": ["Failed to start", "Unit .* failed"],
    "disk": ["No space left on device", "read-only file system"],
    "network": ["Network is unreachable", "Connection timed out"]
    }
    
    NON_ACTIONABLE_KEYWORDS = [
    "ACPI",
    "INTC",
    "intel_ish_ipc",
    "BIOS",
    "Gdm:",
    "bluetoothd",
    "sap-server",
    "gnome-session"
]