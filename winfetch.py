#
import platform
import ops.windows
import ops.linux

def main():
    if platform.system() == "Windows":
        ops.windows.windows_draw()
    elif platform.system() == "Linux":
        ops.linux.linux_draw()
    else:
        print("Unknown platform") 
if __name__ == "__main__":
    main()