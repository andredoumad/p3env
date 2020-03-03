import builtins as _mod_builtins
import srsly.msgpack._ext_type as _mod_srsly_msgpack__ext_type
import srsly.msgpack.exceptions as _mod_srsly_msgpack_exceptions

BufferFull = _mod_srsly_msgpack_exceptions.BufferFull
ExtType = _mod_srsly_msgpack__ext_type.ExtType
ExtraData = _mod_srsly_msgpack_exceptions.ExtraData
FormatError = _mod_srsly_msgpack_exceptions.FormatError
OutOfData = _mod_srsly_msgpack_exceptions.OutOfData
StackError = _mod_srsly_msgpack_exceptions.StackError
class Unpacker(_mod_builtins.object):
    "Streaming unpacker.\n\n    Arguments:\n\n    :param file_like:\n        File-like object having `.read(n)` method.\n        If specified, unpacker reads serialized data from it and :meth:`feed()` is not usable.\n\n    :param int read_size:\n        Used as `file_like.read(read_size)`. (default: `min(1024**2, max_buffer_size)`)\n\n    :param bool use_list:\n        If true, unpack msgpack array to Python list.\n        Otherwise, unpack to Python tuple. (default: True)\n\n    :param bool raw:\n        If true, unpack msgpack raw to Python bytes (default).\n        Otherwise, unpack to Python str (or unicode on Python 2) by decoding\n        with UTF-8 encoding (recommended).\n        Currently, the default is true, but it will be changed to false in\n        near future.  So you must specify it explicitly for keeping backward\n        compatibility.\n\n        *encoding* option which is deprecated overrides this option.\n\n    :param bool strict_map_key:\n        If true, only str or bytes are accepted for map (dict) keys.\n        It's False by default for backward-compatibility.\n        But it will be True from msgpack 1.0.\n\n    :param callable object_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a dict argument after unpacking msgpack map.\n        (See also simplejson)\n\n    :param callable object_pairs_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a list of key-value pairs after unpacking msgpack map.\n        (See also simplejson)\n\n    :param int max_buffer_size:\n        Limits size of data waiting unpacked.  0 means system's INT_MAX (default).\n        Raises `BufferFull` exception when it is insufficient.\n        You should set this parameter when unpacking data from untrusted source.\n\n    :param int max_str_len:\n        Limits max length of str. (default: 1024*1024)\n\n    :param int max_bin_len:\n        Limits max length of bin. (default: 1024*1024)\n\n    :param int max_array_len:\n        Limits max length of array. (default: 128*1024)\n\n    :param int max_map_len:\n        Limits max length of map. (default: 32*1024)\n\n    :param int max_ext_len:\n        Limits max length of map. (default: 1024*1024)\n\n    :param str encoding:\n        Deprecated, use raw instead.\n        Encoding used for decoding msgpack raw.\n        If it is None (default), msgpack raw is deserialized to Python bytes.\n\n    :param str unicode_errors:\n        Error handler used for decoding str type.  (default: `'strict'`)\n\n\n    Example of streaming deserialize from file-like object::\n\n        unpacker = Unpacker(file_like, raw=False)\n        for o in unpacker:\n            process(o)\n\n    Example of streaming deserialize from socket::\n\n        unpacker = Unpacker(raw=False)\n        while True:\n            buf = sock.recv(1024**2)\n            if not buf:\n                break\n            unpacker.feed(buf)\n            for o in unpacker:\n                process(o)\n\n    Raises ``ExtraData`` when *packed* contains extra bytes.\n    Raises ``OutOfData`` when *packed* is incomplete.\n    Raises ``FormatError`` when *packed* is not valid msgpack.\n    Raises ``StackError`` when *packed* contains too nested.\n    Other exceptions can be raised during unpacking.\n    "
    __class__ = Unpacker
    def __init__(self, *args, **kwargs):
        "Streaming unpacker.\n\n    Arguments:\n\n    :param file_like:\n        File-like object having `.read(n)` method.\n        If specified, unpacker reads serialized data from it and :meth:`feed()` is not usable.\n\n    :param int read_size:\n        Used as `file_like.read(read_size)`. (default: `min(1024**2, max_buffer_size)`)\n\n    :param bool use_list:\n        If true, unpack msgpack array to Python list.\n        Otherwise, unpack to Python tuple. (default: True)\n\n    :param bool raw:\n        If true, unpack msgpack raw to Python bytes (default).\n        Otherwise, unpack to Python str (or unicode on Python 2) by decoding\n        with UTF-8 encoding (recommended).\n        Currently, the default is true, but it will be changed to false in\n        near future.  So you must specify it explicitly for keeping backward\n        compatibility.\n\n        *encoding* option which is deprecated overrides this option.\n\n    :param bool strict_map_key:\n        If true, only str or bytes are accepted for map (dict) keys.\n        It's False by default for backward-compatibility.\n        But it will be True from msgpack 1.0.\n\n    :param callable object_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a dict argument after unpacking msgpack map.\n        (See also simplejson)\n\n    :param callable object_pairs_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a list of key-value pairs after unpacking msgpack map.\n        (See also simplejson)\n\n    :param int max_buffer_size:\n        Limits size of data waiting unpacked.  0 means system's INT_MAX (default).\n        Raises `BufferFull` exception when it is insufficient.\n        You should set this parameter when unpacking data from untrusted source.\n\n    :param int max_str_len:\n        Limits max length of str. (default: 1024*1024)\n\n    :param int max_bin_len:\n        Limits max length of bin. (default: 1024*1024)\n\n    :param int max_array_len:\n        Limits max length of array. (default: 128*1024)\n\n    :param int max_map_len:\n        Limits max length of map. (default: 32*1024)\n\n    :param int max_ext_len:\n        Limits max length of map. (default: 1024*1024)\n\n    :param str encoding:\n        Deprecated, use raw instead.\n        Encoding used for decoding msgpack raw.\n        If it is None (default), msgpack raw is deserialized to Python bytes.\n\n    :param str unicode_errors:\n        Error handler used for decoding str type.  (default: `'strict'`)\n\n\n    Example of streaming deserialize from file-like object::\n\n        unpacker = Unpacker(file_like, raw=False)\n        for o in unpacker:\n            process(o)\n\n    Example of streaming deserialize from socket::\n\n        unpacker = Unpacker(raw=False)\n        while True:\n            buf = sock.recv(1024**2)\n            if not buf:\n                break\n            unpacker.feed(buf)\n            for o in unpacker:\n                process(o)\n\n    Raises ``ExtraData`` when *packed* contains extra bytes.\n    Raises ``OutOfData`` when *packed* is incomplete.\n    Raises ``FormatError`` when *packed* is not valid msgpack.\n    Raises ``StackError`` when *packed* contains too nested.\n    Other exceptions can be raised during unpacking.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Unpacker()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def feed(self):
        'Append `next_bytes` to internal buffer.'
        pass
    
    def read_array_header(self):
        'assuming the next object is an array, return its size n, such that\n        the next n unpack() calls will iterate over its contents.\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    
    def read_bytes(self):
        'Read a specified number of raw bytes from the stream'
        pass
    
    def read_map_header(self):
        'assuming the next object is a map, return its size n, such that the\n        next n * 2 unpack() calls will iterate over its key-value pairs.\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    
    def skip(self):
        'Read and ignore one object, returning None\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    
    def tell(self):
        pass
    
    def unpack(self):
        'Unpack one object\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/srsly/msgpack/_unpacker.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'srsly.msgpack._unpacker'
__package__ = 'srsly.msgpack'
__test__ = _mod_builtins.dict()
def default_read_extended_type():
    pass

def ensure_bytes(string):
    'Ensure a string is returned as a bytes object, encoded as utf8.'
    pass

def unpack():
    pass

def unpackb():
    '\n    Unpack packed_bytes to object. Returns an unpacked object.\n\n    Raises ``ExtraData`` when *packed* contains extra bytes.\n    Raises ``ValueError`` when *packed* is incomplete.\n    Raises ``FormatError`` when *packed* is not valid msgpack.\n    Raises ``StackError`` when *packed* contains too nested.\n    Other exceptions can be raised during unpacking.\n\n    See :class:`Unpacker` for options.\n    '
    pass

