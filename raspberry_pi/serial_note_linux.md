##  Notes on attempts to connect usb serial devices

Problem Statement:  Currently the RPLidar can receive power to its motor control and its microchip.  The transmission data and receiving data are not able to be collected or interated with.  The rplidar is not able to be addresses via the serial port (ESL-01) nor via a raspberry pi w gpio interface.   

#### Information on the Serial Ports Linux
- [A linux resource ](https://www.baeldung.com/linux/map-serial-port-dev-tty#:~:text=A%20serial%20port%20is%20a,network%20devices%20to%20a%20computer.)
- [More Serial information](https://www.baeldung.com/linux/all-serial-devices#:~:text=The%20filesystem%20under%20the%20%2Fsys,for%20specific%20serial%20device%20groups.)
- [Details on the Serial Protocol](https://man.freebsd.org/cgi/man.cgi?uart)
- [mac centric details](https://nathancraddock.com/blog/macos-dev-tty-polling/)


#### Command Line Calls
- Indentifying Serial Ports - get or set the configuration of serial port devices
  - ```setserial -g /dev/ttyS* ```
  - gets information about all ../ttyS* devices
- / proc psuedo-filesystem contains info about serial drivers and devices therefor use
  -  ```cat /proc/tty/driver/serial```
- Testing serial ports - read data streams 
  - ```cat /dev/ttyS1```

### Resources
- [ESP-01 pinout](https://www.google.com/search?q=esp+01+wiring+diagram&tbm=isch&ved=2ahUKEwiOrsfVifeDAxUbADQIHZtWCngQ2-cCegQIABAA&oq=esp-01+wir&gs_lcp=CgNpbWcQARgBMgUIABCABDIECAAQHjoECCMQJzoGCAAQBxAeOgYIABAIEB46BggAEAUQHjoHCAAQgAQQGFCsDFiuQWC8TmgBcAB4AYAByQKIAcYGkgEFOC4zLTGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=bI-xZY5Im4DQ8Q-branABw&bih=823&biw=1854#imgrc=-HM-c2HqtvoQEM)
- [Other Users Troubleshooting](https://askubuntu.com/questions/1403705/dev-ttyusb0-not-present-in-ubuntu-22-04)
- [mac troubleshooting](https://stackoverflow.com/questions/12254378/how-to-find-the-serial-port-number-on-mac-os-x)
- 