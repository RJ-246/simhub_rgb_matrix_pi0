Use a Raspberry Pi Zero 2W and the Adafruit RGB Matric Bonnet to drive an RGB Matrix using Simhub


Performance Recommendations from hzeller repo:
- sudo apt-get remove bluez bluez-firmware pi-bluetooth triggerhappy pigpio
- In /boot/firmware/cmdline.txt put the following `isolcpus=domain,managed_irq,3 nohz_full=3 rcu_nocbs=3 irqaffinity=0,1,2`
