from utils import *
from EventManager import Event

class ConstructGraph(Event):
    def __init__(self, graph):
        self.graph = graph


class Axis(Surface):
    def __init__(self, low, high, graph_limit):
        self.low = low
        self.high = high
        self.markings = []
        
        self.calc_markings(graph_limit)
    
    def calc_markings(self, graph_limit):
        scale = (graph_limit)/(self.high-self.low)
        self.markings = [i for i in range(self.low, self.high+1, scale)]
    
    def update(self, event):
        if isinstance(event, ConstructGraph):
            graph = event.graph
            graph.draw(self)

class Graph(Surface):
	def __init_(self):
		raise NotImplementedError
	def plot(self, x, y):
		raise NotImplementedError
	def update(self):
		# Catch The Display Event
		raise NotImplementedError

class XAxis(Axis):
    pass
