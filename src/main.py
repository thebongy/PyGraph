from render.EventManager import EventManager
from render.utils import *
from render.terminal import Terminal
from display.menu import MainMenu
from display.inputhandler import InputHandler

size = Size(120,50)


terminal = Terminal(size)
ev = EventManager()
menu = MainMenu(ev, terminal)

def main():
	while True:
		InputHandler(ev)
main()