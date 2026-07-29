# Docker Container Troubleshooting Runbook

## 1. Container Exited with Code 137 (OOMKilled)
* **Symptom:** Container abruptly stops, `docker ps -a` shows `Exited (137)`.
* **Root Cause:** The Linux kernel Out-Of-Memory (OOM) killer terminated the process because the container exceeded its allocated memory limit.
* **Resolution Steps:**
  1. Inspect container resource usage history: `docker stats --no-stream`
  2. Check kernel logs for OOM events: `dmesg -T | grep -i oom`
  3. Increase memory allocation in `docker-compose.yml` (e.g., `mem_limit: 2g`) or optimize application memory leaks.

## 2. Container Exited with Code 127
* **Symptom:** Container fails to start immediately.
* **Root Cause:** "Command not found" or missing entrypoint binary inside the container filesystem.
* **Resolution Steps:**
  1. Inspect container logs: `docker logs <container_name_or_id>`
  2. Verify entrypoint path in `Dockerfile`.