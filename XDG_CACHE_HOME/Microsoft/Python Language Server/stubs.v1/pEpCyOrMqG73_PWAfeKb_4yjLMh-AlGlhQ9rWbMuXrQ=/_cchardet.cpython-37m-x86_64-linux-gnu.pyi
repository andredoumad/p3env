import builtins as _mod_builtins

class UniversalDetector(_mod_builtins.object):
    __class__ = UniversalDetector
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        pass
    
    @property
    def done(self):
        pass
    
    def feed(self):
        pass
    
    def reset(self):
        pass
    
    @property
    def result(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/cchardet/_cchardet.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'cchardet._cchardet'
__package__ = 'cchardet'
__test__ = _mod_builtins.dict()
def detect_with_confidence():
    pass

