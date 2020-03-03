import builtins as _mod_builtins

B2_ENT = 60
B3_ENT = 59
B4_ENT = 58
def Errors():
    '[__doc__] None'
    pass

I3_ENT = 42
I4_ENT = 41
L2_ENT = 43
L3_ENT = 42
L4_ENT = 41
class PhraseMatcher(_mod_builtins.object):
    'Efficiently match large terminology lists. While the `Matcher` matches\n    sequences based on lists of token descriptions, the `PhraseMatcher` accepts\n    match patterns in the form of `Doc` objects.\n\n    DOCS: https://spacy.io/api/phrasematcher\n    USAGE: https://spacy.io/usage/rule-based-matching#phrasematcher\n    '
    def __call__(self):
        'Find all sequences matching the supplied patterns on the `Doc`.\n\n        doc (Doc): The document to match over.\n        RETURNS (list): A list of `(key, start, end)` tuples,\n            describing the matches. A match tuple describes a span\n            `doc[start:end]`. The `label_id` and `key` are both integers.\n\n        DOCS: https://spacy.io/api/phrasematcher#call\n        '
        pass
    
    __class__ = PhraseMatcher
    def __contains__(self, value):
        'Check whether the matcher contains rules for a match ID.\n\n        key (unicode): The match ID.\n        RETURNS (bool): Whether the matcher contains rules for this match ID.\n\n        DOCS: https://spacy.io/api/phrasematcher#contains\n        '
        return False
    
    def __init__(self):
        'Initialize the PhraseMatcher.\n\n        vocab (Vocab): The shared vocabulary.\n        attr (int / unicode): Token attribute to match on.\n        validate (bool): Perform additional validation when patterns are added.\n        RETURNS (PhraseMatcher): The newly constructed object.\n\n        DOCS: https://spacy.io/api/phrasematcher#init\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Get the number of rules added to the matcher. Note that this only\n        returns the number of rules (identical with the number of IDs), not the\n        number of individual patterns.\n\n        RETURNS (int): The number of rules.\n\n        DOCS: https://spacy.io/api/phrasematcher#len\n        '
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
    def _docs(self):
        pass
    
    @property
    def _patterns(self):
        pass
    
    @property
    def _validate(self):
        pass
    
    def accept_match(self):
        pass
    
    def add(self):
        'Add a match-rule to the phrase-matcher. A match-rule consists of: an ID\n        key, an on_match callback, and one or more patterns.\n\n        key (unicode): The match ID.\n        on_match (callable): Callback executed on match.\n        *docs (Doc): `Doc` objects representing match patterns.\n\n        DOCS: https://spacy.io/api/phrasematcher#add\n        '
        pass
    
    def get_lex_value(self):
        pass
    
    def pipe(self):
        'Match a stream of documents, yielding them in turn.\n\n        docs (iterable): A stream of documents.\n        batch_size (int): Number of documents to accumulate into a working set.\n        return_matches (bool): Yield the match lists along with the docs, making\n            results (doc, matches) tuples.\n        as_tuples (bool): Interpret the input stream as (doc, context) tuples,\n            and yield (result, context) tuples out.\n            If both return_matches and as_tuples are True, the output will\n            be a sequence of ((doc, matches), context) tuples.\n        YIELDS (Doc): Documents, in order.\n\n        DOCS: https://spacy.io/api/phrasematcher#pipe\n        '
        pass
    

U_ENT = 61
def Warnings():
    '[__doc__] None'
    pass

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/spacy/matcher/phrasematcher.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'spacy.matcher.phrasematcher'
__package__ = 'spacy.matcher'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def deprecation_warning(message):
    pass

def get_bilou():
    pass

def unpickle_matcher():
    pass

def user_warning(message):
    pass

