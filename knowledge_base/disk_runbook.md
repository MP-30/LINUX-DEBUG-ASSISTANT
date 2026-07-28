# Linux Disk Space & High I/O Wait Runbook

## 1. Filesystem Full (100% Usage / No Space Left on Device)
* **Symptom:** Disk space at 95%+ or applications throwing `No space left on device` errors.
* **Resolution Steps:**
  1. Check disk space usage across mounts: `df -h`
  2. Identify largest directories: `sudo du -ah /var/log | sort -rh | head -n 10`
  3. Clean up unused Docker resources: `docker system prune -a --volumes`
  4. Truncate oversized syslog/journal logs: `sudo journalctl --vacuum-size=500M`

## 2. High Disk I/O Wait (%iowait)
* **Symptom:** CPU utilization shows high `%iowait` while CPU usage remains low.
* **Resolution Steps:**
  1. Identify processes causing high disk read/write: `sudo iotop -o`
  2. Check disk health and SMART status: `sudo smartctl -a /dev/sda`