from weak_bound_method import WeakBoundMethod

class Event(object):
    pass


class EventManager(object):
    def __init__(self):
        self.listeners = dict()

    def add_listener(self,event,listener):
        '''
        Register a listener for event updates

        Note:
        event is the event CLASS.
        '''
        if event in self.listeners:
            self.listeners[event].append(WeakBoundMethod(listener))
        else:
            self.listeners[event] = [WeakBoundMethod(listener)]
    
    def update(self, event):
        '''
        Update all event listeners about the current event

        Note:
        event is the event OBJECT.
        '''
        for listener in self.listeners[type(event)]:
            listener.update(event)
