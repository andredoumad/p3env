import builtins as _mod_builtins
import spacy.errors as _mod_spacy_errors

def Errors():
    '[__doc__] None'
    pass

IDS = _mod_builtins.dict()
MatchPatternError = _mod_spacy_errors.MatchPatternError
class Matcher(_mod_builtins.object):
    'Match sequences of tokens, based on pattern rules.\n\n    DOCS: https://spacy.io/api/matcher\n    USAGE: https://spacy.io/usage/rule-based-matching\n    '
    def __call__(self):
        'Find all token sequences matching the supplied pattern.\n\n        doc (Doc): The document to match over.\n        RETURNS (list): A list of `(key, start, end)` tuples,\n            describing the matches. A match tuple describes a span\n            `doc[start:end]`. The `label_id` and `key` are both integers.\n        '
        pass
    
    __class__ = Matcher
    def __contains__(self, value):
        'Check whether the matcher contains rules for a match ID.\n\n        key (unicode): The match ID.\n        RETURNS (bool): Whether the matcher contains rules for this match ID.\n        '
        return False
    
    def __init__(self):
        'Create the Matcher.\n\n        vocab (Vocab): The vocabulary object, which must be shared with the\n            documents the matcher will operate on.\n        RETURNS (Matcher): The newly constructed object.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Get the number of rules added to the matcher. Note that this only\n        returns the number of rules (identical with the number of IDs), not the\n        number of individual patterns.\n\n        RETURNS (int): The number of rules.\n        '
        return 0
    
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _callbacks(self):
        pass
    
    @property
    def _extensions(self):
        pass
    
    @property
    def _extra_predicates(self):
        pass
    
    def _normalize_key(self):
        pass
    
    @property
    def _patterns(self):
        pass
    
    def add(self):
        'Add a match-rule to the matcher. A match-rule consists of: an ID\n        key, an on_match callback, and one or more patterns.\n\n        If the key exists, the patterns are appended to the previous ones, and\n        the previous on_match callback is replaced. The `on_match` callback\n        will receive the arguments `(matcher, doc, i, matches)`. You can also\n        set `on_match` to `None` to not perform any actions.\n\n        A pattern consists of one or more `token_specs`, where a `token_spec`\n        is a dictionary mapping attribute IDs to values, and optionally a\n        quantifier operator under the key "op". The available quantifiers are:\n\n        \'!\': Negate the pattern, by requiring it to match exactly 0 times.\n        \'?\': Make the pattern optional, by allowing it to match 0 or 1 times.\n        \'+\': Require the pattern to match 1 or more times.\n        \'*\': Allow the pattern to zero or more times.\n\n        The + and * operators are usually interpretted "greedily", i.e. longer\n        matches are returned where possible. However, if you specify two \'+\'\n        and \'*\' patterns in a row and their matches overlap, the first\n        operator will behave non-greedily. This quirk in the semantics makes\n        the matcher more efficient, by avoiding the need for back-tracking.\n\n        key (unicode): The match ID.\n        on_match (callable): Callback executed on match.\n        *patterns (list): List of token descriptions.\n        '
        pass
    
    def get(self):
        'Retrieve the pattern stored for a key.\n\n        key (unicode or int): The key to retrieve.\n        RETURNS (tuple): The rule, as an (on_match, patterns) tuple.\n        '
        pass
    
    def has_key(self):
        'Check whether the matcher has a rule with a given key.\n\n        key (string or int): The key to check.\n        RETURNS (bool): Whether the matcher has the rule.\n        '
        pass
    
    def pipe(self):
        'Match a stream of documents, yielding them in turn.\n\n        docs (iterable): A stream of documents.\n        batch_size (int): Number of documents to accumulate into a working set.\n        YIELDS (Doc): Documents, in order.\n        '
        pass
    
    def remove(self):
        'Remove a rule from the matcher. A KeyError is raised if the key does\n        not exist.\n\n        key (unicode): The ID of the match rule.\n        '
        pass
    
    @property
    def validator(self):
        pass
    
    @property
    def vocab(self):
        pass
    

TOKEN_PATTERN_SCHEMA = _mod_builtins.dict()
def Warnings():
    '[__doc__] None'
    pass

class _ComparisonPredicate(_mod_builtins.object):
    def __call__(self, token):
        pass
    
    __class__ = _ComparisonPredicate
    __dict__ = {}
    def __init__(self, i, attr, value, predicate, is_extension):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'spacy.matcher.matcher'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    operators = _mod_builtins.tuple()

class _RegexPredicate(_mod_builtins.object):
    def __call__(self, token):
        pass
    
    __class__ = _RegexPredicate
    __dict__ = {}
    def __init__(self, i, attr, value, predicate, is_extension):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'spacy.matcher.matcher'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    operators = _mod_builtins.tuple()

class _SetMemberPredicate(_mod_builtins.object):
    def __call__(self, token):
        pass
    
    __class__ = _SetMemberPredicate
    __dict__ = {}
    def __init__(self, i, attr, value, predicate, is_extension):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'spacy.matcher.matcher'
    def __repr__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    operators = _mod_builtins.tuple()

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/spacy/matcher/matcher.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'spacy.matcher.matcher'
__package__ = 'spacy.matcher'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _get_attr_values():
    pass

def _get_extension_extra_predicates():
    pass

def _get_extensions():
    pass

def _get_extra_predicates():
    pass

def _get_operators():
    pass

def _preprocess_pattern():
    'This function interprets the pattern, converting the various bits of\n    syntactic sugar before we compile it into a struct with init_pattern.\n\n    We need to split the pattern up into three parts:\n    * Normal attribute/value pairs, which are stored on either the token or lexeme,\n        can be handled directly.\n    * Extension attributes are handled specially, as we need to prefetch the\n        values from Python for the doc before we begin matching.\n    * Extra predicates also call Python functions, so we have to create the\n        functions and store them. So we store these specially as well.\n    * Extension attributes that have extra predicates are stored within the\n        extra_predicates.\n    '
    pass

def deprecation_warning(message):
    pass

def get_json_validator(schema):
    pass

def get_string_id():
    "Get a string ID, handling the reserved symbols correctly. If the key is\n    already an ID, return it.\n\n    This function optimises for convenience over performance, so shouldn't be\n    used in tight loops.\n    "
    pass

def unpickle_matcher():
    pass

def validate_json(data, validator):
    'Validate data against a given JSON schema (see https://json-schema.org).\n\n    data: JSON-serializable data to validate.\n    validator (jsonschema.DraftXValidator): The validator.\n    RETURNS (list): A list of error messages, if available.\n    '
    pass

