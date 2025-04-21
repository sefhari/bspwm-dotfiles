import os
from logger import Logger, LoggerStatus

# TODO: !DEPRECATED

class GraphicDrivers:
    @staticmethod
    def build():
        print(f"--The function will be deleted--")
        GraphicDrivers.__prepare_multilib()
        GraphicDrivers.__update_multilib_repo()

    @staticmethod
    def __prepare_multilib():
        Logger.add_record("[+] Prepare Multilib", status=LoggerStatus.SUCCESS)
        os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
        os.system(r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")

    @staticmethod
    def __update_multilib_repo():
        Logger.add_record("[+] Update Multilib Repository", status=LoggerStatus.SUCCESS)
        os.system("sudo pacman -Sl multilib")
        os.system("sudo pacman -Sy")
