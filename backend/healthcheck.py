import psutil
import sys
 
# Vérifie l'utilisation CPU et mémoire
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
 
if cpu_usage > 70 or memory_usage > 70:
    print(f"High usage detected: CPU={cpu_usage:.1f}% MEM={memory_usage:.1f}%")
    sys.exit(1)
else:
    print(f"Healthy: CPU={cpu_usage:.1f}% MEM={memory_usage:.1f}%")
    sys.exit(0)