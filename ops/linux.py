


def linux_draw():
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
    
    class system:
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

    print(system.GPU)
    print("")
    print("                    .88888888:.                      " + typo.BOLD + system.USER+"@"+system.HOST+ typo.END)
    print("                  88888888.88888.                    " + "===========================") 
    print("                .8888888888888888.                   " + "Platform: " +typo.BOLD + system.OS[0] + " " + system.OS[1] + typo.END)
    print("                888888888888888888                   " + "Distribution: " +typo.BOLD + system.DISTRIBUTION[0] + " " + system.DISTRIBUTION[1] + typo.END)
    print("                88' _`88'_  `88888                   " + "Kernel: " +typo.BOLD + system.KERNEL + typo.END)
    print("                88 88 88 88  88888                   " + "Uptime: " +typo.BOLD + str(system.UPTIME) + typo.END)
    print("                88_88_::_88_:88888                   " + "Shell: " +typo.BOLD + system.SHELL + typo.END) 
    print("                88:::,::,:::::8888                   " + "Resolution: " +typo.BOLD + system.RESOLUTION + typo.END)
    print("                88`:::::::::'`8888                   " + "DE: " +typo.BOLD + system.DE + typo.END)
    print("               .88  `::::'    8:88.                  " + "Terminal: " +typo.BOLD + system.TERMINAL + typo.END)
    print("              8888            `8:888.                " + "CPU: " +typo.BOLD + system.CPU + typo.END)
    print("            .8888'             `888888.              " + "GPU: " +typo.BOLD + system.GPU + typo.END) 
    print("           .8888:..  .::.  ...:'8888888:.            " + "Memory: " +typo.BOLD + str(system.MEMORY) + " MB" + typo.END)
    print("          .8888.'     :'     `'::`88:88888           ")
    print("         .8888        '         `.888:8888.          ")
    print("        888:8         .           888:88888          ")
    print("      .888:88        .:           888:88888:         ")
    print("      8888888.       ::           88:888888          ")
    print("      `.::.888.      ::          .88888888           ")
    print("     .::::::.888.    ::         :::`8888'.:.         ")
    print("    ::::::::::.888   '         .::::::::::::         ")
    print("    ::::::::::::.8    '      .:8::::::::::::.        ")
    print("   .::::::::::::::.        .:888:::::::::::::        ")
    print("   :::::::::::::::88:.__..:88888:::::::::::'         ")
    print("    `'.:::::::::::88888888888.88:::::::::'           ")
    print("    `     ':::_:' -- '' -'-' `':_::::'`              ")



  
