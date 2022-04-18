# Windows drawer for Windows.
# This is a snippet from winfetch.py:
# Contains features and solutions for Windows support and information.
def windows_draw():
    #Adding import in function, because winddl auto run on other platforms.
    import os
    import platform
    import ctypes
    import psutil
    import _utils.util as util
    # windows_uptime() is a function that returns the uptime of the windows system.
    def windows_uptime():
        lib = ctypes.windll.kernel32
        t = lib.GetTickCount64()
        t = int(str(t)[:-3])
        mins, sec = divmod(t, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)
        return f"{days} days, {hour:02}:{mins:02}:{sec:02}"
    # The class system is a class that contains the system information of windows system.
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


    # The printing way can be changed for different platforms and logo management.
    print(util.typo.BLUE + "                  ....iilllllllllllll" + util.typo.END + "    " + util.typo.BOLD + system.USERNAME + "@" + system.HOSTNAME + util.typo.END + "")
    print(util.typo.BLUE + "     ....iillll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BLUE+ "========================" + "")
    print(util.typo.BLUE + " iillllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "OS: " + system.OS + " " + system.RELEASE + util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "HOST: " + system.HOSTNAME + util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "Kernel: " + system.KERNEL + util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "Proc: " + system.PROC + util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "GPU: " + system.GPU + util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "Uptime: " + system.UPTIME + util.typo.END + "")
    print("")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "Mem Usage: "+ str(system.MEM_USAGE) +"%"+ util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END + "    " + util.typo.BOLD + "CPU Usage: "+ str(system.CPU_USAGE) +"%"+ util.typo.END + "")
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END)
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END)
    print(util.typo.BLUE + " llllllllllllll   lllllllllllllllllll" + util.typo.END)
    print(util.typo.BLUE + " `^^^^^^lllllll   lllllllllllllllllll" + util.typo.END)
    print(util.typo.BLUE + "       ````^^^^   ^^lllllllllllllllll" + util.typo.END)
    print(util.typo.BLUE + "                       ````^^^^^^llll" + util.ypo.END)
