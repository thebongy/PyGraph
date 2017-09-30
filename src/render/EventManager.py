from weak_bound_method import WeakBoundMethod

class EventManager(object):
    def __init__(self):
        self.listeners = dict()

    def add_listener(self,event,listener):
        if event in self.listeners:
            self.listeners[event].append(WeakBoundMethod(listener))
        else:
            self.listeners[event] = [WeakBoundMethod(listener)]
