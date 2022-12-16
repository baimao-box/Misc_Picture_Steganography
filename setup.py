import os
import time
import sys

print("Please wait a few minutes...")
def mkdir():
	a = os.path.exists("/home/steganography")
	if(a != True):
		os.system("mkdir /home/Steganography")

try:
    os.system("chmod 777 install.sh")
    os.system("./install.sh")
    print("\033[1;31;40mTools and modules installed successfully\033[0m")
except:
    print("\033[1;31;40mInstallation failed\033[0m")
time.sleep(0.8)
try:
    mkdir()
    print("\033[1;31;40mConfiguration and validation files...\033[0m")
    os.system("sudo cp -r tools/BlindWaterMark /home/Steganography/")
    os.system("sudo cp -r tools/cloacked-pixel /home/Steganography/")
    a = os.path.exists("/usr/bin/bwm")
    if(a == True):
        os.system("sudo rm -rf /usr/bin/bwm")
        os.system("sudo rm -rf /usr/bin/lsb")
        os.system("sudo ln -s /home/Steganography/cloacked-pixel/lsb.py /usr/bin/lsb")
        os.system("sudo ln -s /home/Steganography/BlindWaterMark/bwm.py /usr/bin/bwm")
        print("\033[1;31;40mInstallation succeeded\033[0m")
    else:
        os.system("sudo ln -s /home/Steganography/cloacked-pixel/lsb.py /usr/bin/lsb")
        os.system("sudo ln -s /home/Steganography/BlindWaterMark/bwm.py /usr/bin/bwm")
        time.sleep(0.8)
        print("\033[1;31;40mInstallation succeeded\033[0m")
except:
    print("\033[1;31;40mInstallation failed\033[0m")
