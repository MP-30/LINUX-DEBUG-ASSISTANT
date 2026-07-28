# Linux Memory & Swap Exhaustion Runbook

## 1. High RAM Usage & Swap Thrashing
* **Symptom:** Available RAM < 5%, swap usage > 80%, high system responsiveness delay.
* **Root Cause:** High memory demand causing `kswapd0` to constantly move pages between RAM and disk swap.
* **Resolution Steps:**
  1. Find top memory-consuming processes: `ps aux --sort=-%mem | head -n 10`
  2. Check memory usage breakdown: `free -h`
  3. Clear OS page cache (safe temporary relief): `sudo sysctl -w vm.drop_caches=3`
  4. Identify memory leaks in custom background workers or Django/FastAPI processes.