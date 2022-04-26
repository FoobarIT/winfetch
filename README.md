# WINFETCH

For a come back with Python, I decided to clone a quite famous application which is Neofetch. For the moment the script works only on OPS Windows/Linux.

To add distro art follow follow way on ```_utils/distro.py``` and add
condition on racine file ```winfetch.py```.

**In order not to encroach on existing projects the project will be renamed to ```foofetch.py```. The purpose of this project is only to learn more about python and to make you participate if you want.**

# Todo
- Test Distro:
    Debian,
    Windows 10 & 11,
    Fedora,
    Majanro,

- Replace bash command by python stuff.
- Stop doing "One again et bistoufly" way.

# Known Issues
- For windows platform take a long time (3-4s) to display caused by CPU Percent "catcher".

# Change 0.03v
- Now using pkg ```distro``` to detect operating system distribution.
- Using generic function for system info.

# Change 0.02v
- Linux platform support.
- Refactor and comments.             
