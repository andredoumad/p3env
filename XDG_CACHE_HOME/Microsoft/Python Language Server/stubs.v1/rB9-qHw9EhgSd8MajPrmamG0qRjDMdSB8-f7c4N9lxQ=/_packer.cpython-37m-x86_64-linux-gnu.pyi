import builtins as _mod_builtins
import srsly.msgpack._ext_type as _mod_srsly_msgpack__ext_type

ExtType = _mod_srsly_msgpack__ext_type.ExtType
class Packer(_mod_builtins.object):
    "\n    MessagePack Packer\n\n    usage::\n\n        packer = Packer()\n        astream.write(packer.pack(a))\n        astream.write(packer.pack(b))\n\n    Packer's constructor has some keyword arguments:\n\n    :param callable default:\n        Convert user type to builtin type that Packer supports.\n        See also simplejson's document.\n\n    :param bool use_single_float:\n        Use single precision float type for float. (default: False)\n\n    :param bool autoreset:\n        Reset buffer after each pack and return its content as `bytes`. (default: True).\n        If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.\n\n    :param bool use_bin_type:\n        Use bin type introduced in msgpack spec 2.0 for bytes.\n        It also enables str8 type for unicode.\n        Current default value is false, but it will be changed to true\n        in future version.  You should specify it explicitly.\n\n    :param bool strict_types:\n        If set to true, types will be checked to be exact. Derived classes\n        from serializeable types will not be serialized and will be\n        treated as unsupported type and forwarded to default.\n        Additionally tuples will not be serialized as lists.\n        This is useful when trying to implement accurate serialization\n        for python types.\n\n    :param str unicode_errors:\n        Error handler for encoding unicode. (default: 'strict')\n\n    :param str encoding:\n        (deprecated) Convert unicode to bytes with this encoding. (default: 'utf-8')\n    "
    __class__ = Packer
    def __init__(self, *args, **kwargs):
        "\n    MessagePack Packer\n\n    usage::\n\n        packer = Packer()\n        astream.write(packer.pack(a))\n        astream.write(packer.pack(b))\n\n    Packer's constructor has some keyword arguments:\n\n    :param callable default:\n        Convert user type to builtin type that Packer supports.\n        See also simplejson's document.\n\n    :param bool use_single_float:\n        Use single precision float type for float. (default: False)\n\n    :param bool autoreset:\n        Reset buffer after each pack and return its content as `bytes`. (default: True).\n        If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.\n\n    :param bool use_bin_type:\n        Use bin type introduced in msgpack spec 2.0 for bytes.\n        It also enables str8 type for unicode.\n        Current default value is false, but it will be changed to true\n        in future version.  You should specify it explicitly.\n\n    :param bool strict_types:\n        If set to true, types will be checked to be exact. Derived classes\n        from serializeable types will not be serialized and will be\n        treated as unsupported type and forwarded to default.\n        Additionally tuples will not be serialized as lists.\n        This is useful when trying to implement accurate serialization\n        for python types.\n\n    :param str unicode_errors:\n        Error handler for encoding unicode. (default: 'strict')\n\n    :param str encoding:\n        (deprecated) Convert unicode to bytes with this encoding. (default: 'utf-8')\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bytes(self):
        'Return internal buffer contents as bytes object'
        pass
    
    def getbuffer(self):
        'Return view of internal buffer.'
        pass
    
    def pack(self):
        pass
    
    def pack_array_header(self):
        pass
    
    def pack_ext_type(self):
        pass
    
    def pack_map_header(self):
        pass
    
    def pack_map_pairs(self):
        '\n        Pack *pairs* as msgpack map type.\n\n        *pairs* should be a sequence of pairs.\n        (`len(pairs)` and `for k, v in pairs:` should be supported.)\n        '
        pass
    
    def reset(self):
        'Reset internal buffer.\n\n        This method is usaful only when autoreset=False.\n        '
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/srsly/msgpack/_packer.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'srsly.msgpack._packer'
__package__ = 'srsly.msgpack'
__test__ = _mod_builtins.dict()
def ensure_bytes(string):
    'Ensure a string is returned as a bytes object, encoded as utf8.'
    pass

