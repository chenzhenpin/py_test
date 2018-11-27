#python2 psutil 
#coding=utf-8

import psutil
mem = psutil.virtual_memory()
psutil.swap_memory()
print(psutil.net_io_counters())
print(psutil.pids())
print(psutil.Process(780).name)
print(psutil.Process(780).create_time())

print(psutil.cpu_times())
#print(psutil.cpu_count(logical=False))
print(psutil.cpu_count())
print (mem.total)
print (mem.used)
print(float(int(mem.used)/int(mem.total)))