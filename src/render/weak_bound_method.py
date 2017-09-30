from weakref import ref

class WeakBoundMethod(object):
    def __init__(self,method):
        self._self = ref(method.__self)
        self._func = method.__func__

    def __call__(self,*args,**kwargs):
        self._func(self._self(), *args, **kwargs)
