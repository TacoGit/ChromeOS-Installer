# 🚀 Stock ChromeOS Installer for non ChromeOS devices
# 💬 All the download links are from github and cros.tech, these are what we need

# ⚡ Import needs
from shutil import which
from time import time
from colorama import Fore, Back, Style
import requests
import sys
import shutil
import time
import os
import zipfile

# ⚡ Initialize colorama
from colorama import init
init()

# 📝 This project is mostly made for windows user, please change this line to your current operating system to make it function properly.
def cls():
    os.system('cls')

# 💬 Main UI
def main():
    cls()
    
    print(Style.RESET_ALL)

    print(Fore.WHITE + '         An easy ' + Fore.BLUE + 'Chrome' + Fore.WHITE + "OS installer for non ChromeOS devices")
    print("                     Last updated " + Fore.LIGHTBLUE_EX + "2022 July 24")

    print(Style.RESET_ALL)

    if len(sys.argv) == 1:
        print("                  Please run this program with args")
        print("'py "  + sys.argv[0] + " download' to download the needs [ANY](Download to current dir)")
        print("'py "  + sys.argv[0] + " install' to install the operating system [LINUX](Dualboot to partition only)")
        print("'py "  + sys.argv[0] + " after_install' to see what to do after installed [WINDOWS]")
        print(Style.RESET_ALL)
        os._exit(0)

    if str(sys.argv[1]) == "download":
        print("               Please type in what intel cpu you have.")
        print("    If your cpu isnt listed below, this program isnt made for you")

        print(Style.RESET_ALL)

        cpu = str(input("                  [options: i3, i5, i7]: " + Fore.LIGHTBLUE_EX))
        print(Style.RESET_ALL)
        cpu = cpu.lower()

        if cpu != "i3":
            if cpu != "i5":
                if cpu != "i7":
                    print("      Canceled, your cpu did not meet the requirements")
                    print("                    Your cpu: " + str(cpu))
                    os._exit(0)

        print("Starting downloads in 5 seconds, exit the program if u do not wish to download the files")
        print("      You will need atleast 8gb free space and a stable internet connection.")

        time.sleep(0)
        
        cls()

        print(Style.RESET_ALL)

        namecolor = Fore.RED + 'Ch' + Fore.GREEN + 'r' + Fore.BLUE + 'o' + Fore.YELLOW + 'me'

        print(Fore.WHITE + '         An easy ' + Fore.BLUE + 'Chrome' + Fore.WHITE + "OS installer for non ChromeOS devices")
        print("                     Last updated " + Fore.LIGHTBLUE_EX + "2022 July 24")

        print(Style.RESET_ALL)

        print("[Step 1/4] Downloading 'rammus' v101 image from cros.tech (This may take a while)")
        open('cache/chromeos_14588.98.0_rammus_recovery_stable-channel_mp-v2.bin.zip', 'wb').write(requests.get('https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_14588.98.0_rammus_recovery_stable-channel_mp-v2.bin.zip', allow_redirects=True).content)
        print("[Step 2/4] Downloading 'brunch' from github.com (This may take a while)")
        open('cache/brunch.tar.gz', 'wb').write(requests.get('https://github.com/sebanc/brunch/releases/download/r103-stable-20220721/brunch_r103_stable_20220721.tar.gz', allow_redirects=True).content)
        
        print("[Step 3/4] Extracting image zip (This may take a while)")
        with zipfile.ZipFile("cache/chromeos_14588.98.0_rammus_recovery_stable-channel_mp-v2.bin.zip", 'r') as zip_ref:
            zip_ref.extractall("cache/")

        print("[Step 4/4] Full extracting brunch zip (This may take a while)")
        with zipfile.ZipFile("cache/brunch.tar.gz", 'r') as zip_ref:
            zip_ref.extractall("cache/")
        with zipfile.ZipFile("cache/brunch.tar", 'r') as zip_ref:
            zip_ref.extractall("cache/")

        print("[ Congrats ] All files have been downloaded and extracted successfully")
        print(Style.RESET_ALL)
        print("[ INFO ] If you currently have WSL2 or a prepared linux machine, type 'py "  + sys.argv[0] + " install' for further instructions")
    
    if str(sys.argv[1]) == "install":
        # Manually you would have to type long stuff like "sudo bash chromeos-install.sh -src IMAGE.BIN -dst DRIVE/DIRECTORY_TO_INSTALL_TO -s SIZE"

        try:
            if not os.path.exists("cache"):
                print("Please go through the downloads first, do not touch the cache folder after that.")
                os._exit(0)
        except:
            print("Please go through the downloads first, do not touch the cache folder after that.")
        
        print("Installing ChromeOS requires linux, make sure you are on a WSL2 or a Linux Machine")
        print("Please make sure 'cache/chromeos-install.sh' is and stays untouched")
        time.sleep(1)
        os.system("ls cache/")
        time.sleep(0.5)
        bin = str(input("Please copy paste the bin file name with the extension (EX: 'RAMMUS.BIN'): "))
        drive_to_install_to = str(input("[MAKE SURE ITS MOUNTED] Please copy paste the drive to install to (EX: '/media/ubuntu/ChromeOS'): "))
        part_size = str(input("[MAKE SURE ITS MOUNTED] Drive partition size in GB? (Minimum 20) (EX: '20'): "))
        print(Style.RESET_ALL)

        command = "sudo bash chromeos-install.sh -src " + bin + " -dst " + drive_to_install_to + " -s " + part_size
        commandAlt = "sudo bash chromeos-install.sh -src " + bin + " -dst " + drive_to_install_to + "/chromeos -s " + part_size
        command = str(command)
        commandAlt = str(commandAlt)

        print("cd cache/")

        print(command)
        print("OR")
        print(commandAlt)

        print(Style.RESET_ALL)

        print("Type 1 to automatically run the command (Not recommended)")
        print("Type 2 to exit and run the command manually (Mostly recommended)")
        if str(input("[Options: 1,2]: ")) == "1":
            os.system(command)
            print("Please view 'py "  + sys.argv[0] + " after_install' after and than your all set!")
        else:
            print("Please view 'py "  + sys.argv[0] + " after_install' after and than your all set!")
            os._exit(1)
        
    if str(sys.argv[1]) == "after_install":
        print("After you installed, you can see that the operating system is not listed in the boot menu")
        print("These steps are only for Windows, this might be possible for Ubuntu too, i do not know how")
        print("Please follow these steps to add it to the boot menu:")
        print(Style.RESET_ALL)
        print("[1/6] Download and install Grub2Win")
        print("On some debloated windows operating system, you will receive a 'Regedit' error after launching/installing the program, ignore this. No harm done")
        print("[2/6] On the partition/drive you installed the ChromeOS file to, there must be a text file made called 'chromeos.grub.txt' open this and copy")
        print("[3/6] Open grub2win, press 'Manage Boot Menu', its a yellow button at the bottom")
        print("[4/6] Press the orange button at the top called 'Add New Entry'")
        print("[5/6] A big orange box is opened, at the top left there is a something called 'Type:', open it and press 'Custom Code'")
        print("[6/6] Paste the code u copied earlier at step 2, press Apply and OK. Make sure grub2win is set at default boot EFI manager")
        print("You may configurate the theme yourself, nothing will harm for changing themes")

# 🔧 If you are here to change code, this is the best thing u can change
main()
