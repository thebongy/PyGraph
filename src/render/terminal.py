import platform
from subsystem import call

class Terminal(object):
    def __init__(self,size):
        self.os = platform.system() # Get the User's Operating System

        if self.os == "Windows":
            self.clear_command = "cls"
            self.resize_command = "mode %(width)s,%(height)s"
        else:
            self.clear_command = "clear"
            self.resize_command = "printf '\e[8;%(height)s;%(width)st'"
        
        self.resize_screen(size)
        self.clear_screen()

    def clear_screen(self):
        # Clear Terminal/CMD screen
        call([self.clear_command])

    def resize_screen(self,size):
        call([self.resize_command % size])

