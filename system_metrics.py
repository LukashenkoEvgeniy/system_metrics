import psutil
import sys


def get_cpu_info():
    print('system.cpu.idle', psutil.cpu_times().idle)
    print('system.cpu.user', psutil.cpu_times().user)
    print('system.cpu.guest', psutil.cpu_times().guest)
    print('system.cpu.iowait', psutil.cpu_times().iowait)
    print('system.cpu.stolen', psutil.cpu_times().steal)
    print('system.cpu.system ', psutil.cpu_times().system)


def get_memory_info():
    print('virtual total ', psutil.virtual_memory().total)
    print('virtual used ', psutil.virtual_memory().used)
    print('virtual free ', psutil.virtual_memory().free)
    print('virtual shared ', psutil.virtual_memory().shared)
    print('swap total ', psutil.swap_memory().total)
    print('swap used ', psutil.swap_memory().used)
    print('swap free ', psutil.swap_memory().free)


if sys.argv[1] != "mem" and sys.argv[1] != "cpu":
    print("No such argument")

if len(sys.argv) <= 1:
    print("Enter param 'cpu' or 'mem' to get metrics")
    quit()

if sys.argv[1] == "cpu":
    get_cpu_info()

if sys.argv[1] == "mem":
    get_memory_info()
