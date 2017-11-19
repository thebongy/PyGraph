import platform
from os import system

class Terminal(object):
    def __init__(self,size):
        self.os = platform.system() # Get the User's Operating System

        if self.os == "Windows":
            self.clear_command = "cls"
            self.resize_command = "mode %s,%s" % (size.width, size.height)
        else:
            self.clear_command = "clear"
            self.resize_command = "printf '\e[8;%s;%st'" % (size.height, size.width)
        
        self.resize_screen(size)
        self.clear_screen()

    def clear_screen(self):
        # Clear Terminal/CMD screen
        system(self.clear_command)

    def resize_screen(self,size):
        system(self.resize_command)

