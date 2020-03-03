import builtins as _mod_builtins
import socket as _mod_socket

ARES_EADDRGETNETWORKPARAMS = 23
ARES_EBADFAMILY = 9
ARES_EBADFLAGS = 18
ARES_EBADHINTS = 20
ARES_EBADNAME = 8
ARES_EBADQUERY = 7
ARES_EBADRESP = 10
ARES_EBADSTR = 17
ARES_ECANCELLED = 24
ARES_ECONNREFUSED = 11
ARES_EDESTRUCTION = 16
ARES_EFILE = 14
ARES_EFORMERR = 2
ARES_ELOADIPHLPAPI = 22
ARES_ENODATA = 1
ARES_ENOMEM = 15
ARES_ENONAME = 19
ARES_ENOTFOUND = 4
ARES_ENOTIMP = 5
ARES_ENOTINITIALIZED = 21
ARES_EOF = 13
ARES_EREFUSED = 6
ARES_ESERVFAIL = 3
ARES_ETIMEOUT = 12
ARES_FLAG_IGNTC = 4
ARES_FLAG_NOALIASES = 64
ARES_FLAG_NOCHECKRESP = 128
ARES_FLAG_NORECURSE = 8
ARES_FLAG_NOSEARCH = 32
ARES_FLAG_PRIMARY = 2
ARES_FLAG_STAYOPEN = 16
ARES_FLAG_USEVC = 1
ARES_SUCCESS = 0
class InvalidIP(_mod_builtins.ValueError):
    __class__ = InvalidIP
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'gevent.resolver.cares'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

TIMEOUT = 1
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/gevent/resolver/cares.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'gevent.resolver.cares'
__package__ = 'gevent.resolver'
__test__ = _mod_builtins.dict()
_ares_errors = _mod_builtins.dict()
_cares_flag_map = None
def _convert_cares_flags():
    pass

class ares_host_result(_mod_builtins.tuple):
    __class__ = ares_host_result
    __dict__ = {}
    def __getnewargs__(self):
        return ()
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'gevent.resolver.cares'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class channel(_mod_builtins.object):
    __class__ = channel
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _getnameinfo(self):
        pass
    
    def _on_timer(self):
        pass
    
    def _process_fd(self):
        pass
    
    @property
    def _timer(self):
        pass
    
    @property
    def _watchers(self):
        pass
    
    def destroy(self):
        pass
    
    def gethostbyaddr(self):
        pass
    
    def gethostbyname(self):
        pass
    
    def getnameinfo(self):
        pass
    
    @property
    def loop(self):
        pass
    
    def set_servers(self):
        pass
    

gaierror = _mod_socket.gaierror
class result(_mod_builtins.object):
    __class__ = result
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def exception(self):
        pass
    
    def get(self):
        pass
    
    def successful(self):
        pass
    
    @property
    def value(self):
        pass
    

def strerror():
    pass

