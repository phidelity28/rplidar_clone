# Raspberry Pi (RP or rp in this doc going forward)

## Login 
- User Name : peek-py
- Password: aric2024

## General Information
- Model : Raspberry Pi 4 Model B w GPIO extension board:  The testing with this device is to evaluate whether it can be a hardware/ software system for controlling and extracting the lidar data from a RPLidar A1M8.  This data will be use to build a 3D representation (point cloud)  of dimensinal lumber on a industrial conveyor system.
- [RPLidar Python Documentation](https://rplidar.readthedocs.io/en/latest/)  
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)



## Installation Details and Notes on Raspberry 
- 32 gb micro sd was flashed via Balena Etcher and a download of the latest os image because mac osx 10.13 would not run the current image and flash software.
- 2023-12-05 Raspios-bookworm-arm.img.xy
- the USB-Micro port is power only and the unit has both a red led to indicate power and green to indicate cpu activity during boot
- python3 --version = 3.11
- sudo apt install code = vscode 1.83
- !! Key note from RP docs :' in previous version of rp it was possible to -> $ pip install numpy( or any library) this is now disallowed.  If you try to install a package system-wide you will receive an error. "error: externally managed environment".  This is due to long standing conflicts of sytem wide OS package managers  like apt vs Python-specific package managers like pip.  If you want specific python packages you must do it in the venv'
- vscode is setup to my personal account which means all extensions are synced for my choices
  - C/C++ ext pack
  - pylance
  - md preview/ md all in one
  - jupyter
  - javascrip es6 code snippet
- git --version 2.39.2
- set up venv:  python3.11 -m venv rasp_venv -> ($ source rasp_venv/activate/bin)
- some basic libraries were added - numpy, click, serial and gpiozero (this is the library that is necessary to interact with the GPIO electronics)
  