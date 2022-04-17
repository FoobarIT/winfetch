#! 
import os
import platform
import ctypes
import psutil


def windows_uptime():
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    return f"{days} days, {hour:02}:{mins:02}:{sec:02}"


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


class system:
    USERNAME = os.environ.get('USERNAME')
    HOSTNAME = os.getenv('COMPUTERNAME')
    OS = platform.system()
    KERNEL = platform.uname()[3]
    RELEASE = platform.release()
    UPTIME = windows_uptime()
    PROC = platform.processor()
    GPU = platform.uname()[4]
    MEM_USAGE = psutil.virtual_memory()[2] # (total, available, percent, used, free, active, inactive, wired)
    CPU_USAGE = psutil.cpu_percent(4)


print(typo.BLUE + "                  ....iilllllllllllll" + typo.END + "    " + typo.BOLD + system.USERNAME + "@" + system.HOSTNAME + typo.END + "")
print(typo.BLUE + "     ....iillll   lllllllllllllllllll" + typo.END + "    " + typo.BLUE+ "========================" + "")
print(typo.BLUE + " iillllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "OS: " + system.OS + " " + system.RELEASE + typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "HOST: " + system.HOSTNAME + typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "Kernel: " + system.KERNEL + typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "Proc: " + system.PROC + typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "GPU: " + system.GPU + typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "Uptime: " + system.UPTIME + typo.END + "")
print("")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "Mem Usage: "+ str(system.MEM_USAGE) +"%"+ typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END + "    " + typo.BOLD + "CPU Usage: "+ str(system.CPU_USAGE) +"%"+ typo.END + "")
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll   lllllllllllllllllll" + typo.END)
print(typo.BLUE + " `^^^^^^lllllll   lllllllllllllllllll" + typo.END)
print(typo.BLUE + "       ````^^^^   ^^lllllllllllllllll" + typo.END)
print(typo.BLUE + "                       ````^^^^^^llll" + typo.END)
