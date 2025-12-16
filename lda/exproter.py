import time
from prometheus_client import start_http_server, Gauge


cpu_usage = Gauge("system_cpu_usage_percent", "CPU usage percentage")
memory_usage = Gauge("system_memory_usage_percent", "Memory usage percentage")


def read_cpu():
   with open("/proc/stat") as f:
       parts = f.readline().split()[1:]
       values = list(map(int, parts))
       idle = values[3] + values[4]
       total = sum(values)
       return idle, total
  
prev_idle, prev_total = read_cpu()


def collect():
   global prev_idle, prev_total
   idle, total = read_cpu()
   idle_delta = idle -prev_idle
   total_delta = total-prev_total
   cpu = 100 * (1- idle_delta / total_delta)
   prev_idle , prev_total = idle, total
   return cpu


def read_mem():
   with open("/proc/meminfo")as f:
       mem = {}
       for line in f:
           k , v = line.split(":")
           mem[k] = int(v.split()[0])
   return 100 * (1 - mem["MemAvailable"] / mem["MemTotal"])


if __name__ == "__main__":
   start_http_server(8000)
   while True:
       cpu_usage.set(collect())
       memory_usage.set(read_mem())
       time.sleep(1)

