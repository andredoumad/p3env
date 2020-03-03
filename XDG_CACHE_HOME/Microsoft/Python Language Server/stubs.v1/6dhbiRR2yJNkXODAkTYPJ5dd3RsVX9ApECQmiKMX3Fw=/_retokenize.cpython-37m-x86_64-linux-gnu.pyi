import builtins as _mod_builtins
import spacy.util as _mod_spacy_util

def Errors():
    '[__doc__] None'
    pass

class Retokenizer(_mod_builtins.object):
    'Helper class for doc.retokenize() context manager.\n\n    DOCS: https://spacy.io/api/doc#retokenize\n    USAGE: https://spacy.io/usage/linguistic-features#retokenization\n    '
    __class__ = Retokenizer
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __init__(self):
        'Helper class for doc.retokenize() context manager.\n\n    DOCS: https://spacy.io/api/doc#retokenize\n    USAGE: https://spacy.io/usage/linguistic-features#retokenization\n    '
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
    
    def merge(self):
        'Mark a span for merging. The attrs will be applied to the resulting\n        token.\n\n        span (Span): The span to merge.\n        attrs (dict): Attributes to set on the merged token.\n\n        DOCS: https://spacy.io/api/doc#retokenizer.merge\n        '
        pass
    
    def split(self):
        'Mark a Token for splitting, into the specified orths. The attrs\n        will be applied to each subtoken.\n\n        token (Token): The token to split.\n        orths (list): The verbatim text of the split tokens. Needs to match the\n            text of the original token.\n        heads (list): List of token or `(token, subtoken)` tuples specifying the\n            tokens to attach the newly split subtokens to.\n        attrs (dict): Attributes to set on all split tokens. Attribute names\n            mapped to list of per-token attribute values.\n\n        DOCS: https://spacy.io/api/doc#retokenizer.split\n        '
        pass
    

SimpleFrozenDict = _mod_spacy_util.SimpleFrozenDict
__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/spacy/tokens/_retokenize.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'spacy.tokens._retokenize'
__package__ = 'spacy.tokens'
def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Retokenizer():
    pass

__test__ = _mod_builtins.dict()
def _bulk_merge():
    "Retokenize the document, such that the spans described in 'merges'\n     are merged into a single token. This method assumes that the merges\n     are in the same order at which they appear in the doc, and that merges\n     do not intersect each other in any way.\n\n    merges: Tokens to merge, and corresponding attributes to assign to the\n        merged token. By default, attributes are inherited from the\n        syntactic root of the span.\n    RETURNS (Token): The first newly merged token.\n    "
    pass

def _merge():
    'Retokenize the document, such that the span at\n    `doc.text[start_idx : end_idx]` is merged into a single token. If\n    `start_idx` and `end_idx `do not mark start and end token boundaries,\n    the document remains unchanged.\n    start_idx (int): Character index of the start of the slice to merge.\n    end_idx (int): Character index after the end of the slice to merge.\n    **attributes: Attributes to assign to the merged token. By default,\n        attributes are inherited from the syntactic root of the span.\n    RETURNS (Token): The newly merged token, or `None` if the start and end\n        indices did not fall at token boundaries.\n    '
    pass

def _resize_tensor():
    pass

def _split():
    "Retokenize the document, such that the token at\n    `doc[token_index]` is split into tokens with the orth 'orths'\n    token_index(int): token index of the token to split.\n    orths: IDs of the verbatim text content of the tokens to create\n    **attributes: Attributes to assign to each of the newly created tokens. By default,\n        attributes are inherited from the original token.\n    RETURNS (Token): The first newly created token.\n    "
    pass

def _validate_extensions():
    pass

def get_array_module(_):
    pass

def get_string_id():
    "Get a string ID, handling the reserved symbols correctly. If the key is\n    already an ID, return it.\n\n    This function optimises for convenience over performance, so shouldn't be\n    used in tight loops.\n    "
    pass

def intify_attrs():
    '\n    Normalize a dictionary of attributes, converting them to ints.\n\n    stringy_attrs (dict): Dictionary keyed by attribute string names. Values\n        can be ints or strings.\n    strings_map (StringStore): Defaults to None. If provided, encodes string\n        values into ints.\n    RETURNS (dict): Attributes dictionary with keys and optionally values\n        converted to ints.\n    '
    pass

def is_writable_attr(ext):
    'Check if an extension attribute is writable.\n    ext (tuple): The (default, getter, setter, method) tuple available  via\n        {Doc,Span,Token}.get_extension.\n    RETURNS (bool): Whether the attribute is writable.\n    '
    pass

