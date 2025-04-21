import os
from logger import Logger, LoggerStatus


class AurBuilder:
    @staticmethod
    def build():
        os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
        os.system("cd /tmp/yay && makepkg -si")


class FirefoxCustomize:
    @staticmethod
    def build():
        os.system("timeout 10 firefox --headless")
        os.system("sh firefox/install.sh")
        Logger.add_record(f"[+] Firefox styles installed", status=LoggerStatus.SUCCESS)


class OhMyZSH:
    @staticmethod
    def build():
        os.system("sh -c '$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")
        Logger.add_record(f"[+] Oh my ZSH installed", status=LoggerStatus.SUCCESS)

class Chaotic:
    @staticmethod
    def build():
        os.system("sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com")
        os.system("sudo pacman-key --lsign-key 3056513887B78AEB")
        os.system("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'")
        os.system("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
        with open('/etc/pacman.conf', 'a') as file:
            file.write('[chaotic-aur]')
            file.write('Include = /etc/pacman.d/chaotic-mirrorlist')
