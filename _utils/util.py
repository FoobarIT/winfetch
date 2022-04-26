import os
import platform
import distro
from cpuinfo import get_cpu_info

class typo:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Work actually on ubuntu : waiting of other distribution testing.
class linux_info:
    USER = os.getlogin()
    HOST = platform.uname()[1]
    OS = platform.system(), platform.release()
    DISTRIBUTION = distro.linux_distribution()
    KERNEL = platform.uname()[2]
    UPTIME = os.popen('uptime -p').read()[:-1]
    SHELL = os.getenv('SHELL')
    RESOLUTION = os.popen('xrandr | grep "*"').read().split()[0]
    DE = os.popen('cat /etc/os-release | grep "PRETTY_NAME"').read().split('"')[1]
    TERMINAL = os.getenv('TERM')
    CPU = get_cpu_info()['brand_raw']
    GPU = os.popen("lspci -v | egrep -i '3d'").read()[23:-1]
    MEMORY = os.popen('cat /proc/meminfo | grep MemTotal').read().split()[1]
