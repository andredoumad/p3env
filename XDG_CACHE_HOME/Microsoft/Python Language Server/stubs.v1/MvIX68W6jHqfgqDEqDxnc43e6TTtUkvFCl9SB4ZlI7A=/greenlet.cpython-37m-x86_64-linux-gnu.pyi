import builtins as _mod_builtins

GREENLET_USE_GC = True
GREENLET_USE_TRACING = True
class GreenletExit(_mod_builtins.BaseException):
    __class__ = GreenletExit
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'greenlet'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

_C_API = _mod_builtins.PyCapsule()
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/greenlet.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'greenlet'
__package__ = ''
__version__ = '0.4.15'
class error(_mod_builtins.Exception):
    __class__ = error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'greenlet'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def getcurrent():
    pass

def gettrace():
    pass

class greenlet(_mod_builtins.object):
    'greenlet(run=None, parent=None) -> greenlet\n\nCreates a new greenlet object (without running it).\n\n - *run* -- The callable to invoke.\n - *parent* -- The parent greenlet. The default is the current greenlet.'
    GreenletExit = GreenletExit()
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = greenlet
    __dict__ = {}
    def __getstate__(self):
        pass
    
    def __init__(self, run=None, parent=None):
        'greenlet(run=None, parent=None) -> greenlet\n\nCreates a new greenlet object (without running it).\n\n - *run* -- The callable to invoke.\n - *parent* -- The parent greenlet. The default is the current greenlet.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _stack_saved(self):
        pass
    
    @property
    def dead(self):
        pass
    
    error = error()
    @classmethod
    def getcurrent(cls):
        pass
    
    @classmethod
    def gettrace(cls):
        pass
    
    @property
    def gr_frame(self):
        pass
    
    @property
    def parent(self):
        pass
    
    @property
    def run(self):
        pass
    
    @classmethod
    def settrace(cls):
        pass
    
    def switch(self, *args, **kwargs):
        "switch(*args, **kwargs)\n\nSwitch execution to this greenlet.\n\nIf this greenlet has never been run, then this greenlet\nwill be switched to using the body of self.run(*args, **kwargs).\n\nIf the greenlet is active (has been run, but was switch()'ed\nout before leaving its run function), then this greenlet will\nbe resumed and the return value to its switch call will be\nNone if no arguments are given, the given argument if one\nargument is given, or the args tuple and keyword args dict if\nmultiple arguments are given.\n\nIf the greenlet is dead, or is the current greenlet then this\nfunction will simply return the arguments using the same rules as\nabove.\n"
        pass
    
    def throw(self):
        'Switches execution to the greenlet ``g``, but immediately raises the\ngiven exception in ``g``.  If no argument is provided, the exception\ndefaults to ``greenlet.GreenletExit``.  The normal exception\npropagation rules apply, as described above.  Note that calling this\nmethod is almost equivalent to the following::\n\n    def raiser():\n        raise typ, val, tb\n    g_raiser = greenlet(raiser, parent=g)\n    g_raiser.switch()\n\nexcept that this trick does not work for the\n``greenlet.GreenletExit`` exception, which would not propagate\nfrom ``g_raiser`` to ``g``.\n'
        pass
    

def settrace():
    pass

