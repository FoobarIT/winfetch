import os
import sys
import platform
import ctypes
 
def windows_uptime():
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    return (f"{days} days, {hour:02}:{mins:02}:{sec:02}")

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
    OS_RELEASE = platform.release()
    OS_UPTIME = windows_uptime()

print(os.name()[2])

print(typo.BLUE + "                 ....iilllllllllllll" + typo.END + "          "+typo.BOLD+ system.USERNAME +"@"+ system.HOSTNAME + typo.END+"")
print(typo.BLUE + "     ....iillll  lllllllllllllllllll" + typo.END + "          =====================")
print(typo.BLUE + " iillllllllllll  lllllllllllllllllll" + typo.END + "          "+typo.BOLD +"OS: "+system.OS+" "+system.OS_RELEASE+typo.END+"")
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END + "          "+typo.BOLD +"HOST: "+system.HOSTNAME+typo.END+"")
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END + "          "+typo.BOLD +"Uptime: "+system.OS_UPTIME+typo.END+"")
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + "" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " llllllllllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + " `^^^^^^lllllll  lllllllllllllllllll" + typo.END)
print(typo.BLUE + "       ````^^^^  ^^lllllllllllllllll" + typo.END)
print(typo.BLUE + "                      ````^^^^^^llll" + typo.END)

