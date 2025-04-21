import os


class Daemons:
    @staticmethod
    def enable_all_daemons():
        Daemons.__enable_network_daemon()

    @staticmethod
    def __enable_network_daemon():
        os.system("sudo systemctl enable NetworkManager")
