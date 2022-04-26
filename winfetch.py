#
import distro
import _utils.distro
from _utils.util import linux_info
linuxInfo = linux_info()


def main():
    print(distro.id())
    if distro.id() == "windows":
        pass
    elif distro.id() == "ubuntu":
        # Add arguments
        _utils.distro.ubuntu(
            linuxInfo.USER,
            linuxInfo.HOST,
            linuxInfo.OS,
            linuxInfo.DISTRIBUTION,
            linuxInfo.KERNEL,
            linuxInfo.UPTIME,
            linuxInfo.SHELL,
            linuxInfo.RESOLUTION,
            linuxInfo.DE,
            linuxInfo.TERMINAL,
            linuxInfo.CPU,
            linuxInfo.GPU,
            linuxInfo.MEMORY);
    else:
        print("Unknown platform")
if __name__ == "__main__":
    main()
