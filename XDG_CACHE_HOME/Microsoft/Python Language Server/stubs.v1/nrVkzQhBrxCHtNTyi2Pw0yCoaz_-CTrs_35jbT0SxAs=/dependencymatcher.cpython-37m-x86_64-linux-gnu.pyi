import builtins as _mod_builtins

DELIMITER = '||'
class DependencyTreeMatcher(_mod_builtins.object):
    'Match dependency parse tree based on pattern rules.'
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = DependencyTreeMatcher
    def __contains__(self, value):
        'Check whether the matcher contains rules for a match ID.\n\n        key (unicode): The match ID.\n        RETURNS (bool): Whether the matcher contains rules for this match ID.\n        '
        return False
    
    def __init__(self):
        'Create the DependencyTreeMatcher.\n\n        vocab (Vocab): The vocabulary object, which must be shared with the\n            documents the matcher will operate on.\n        RETURNS (DependencyTreeMatcher): The newly constructed object.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Get the number of rules, which are edges, added to the dependency\n        tree matcher.\n\n        RETURNS (int): The number of rules.\n        '
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
    def _entities(self):
        pass
    
    @property
    def _keys_to_token(self):
        pass
    
    @property
    def _nodes(self):
        pass
    
    def _normalize_key(self):
        pass
    
    @property
    def _patterns(self):
        pass
    
    @property
    def _root(self):
        pass
    
    @property
    def _tree(self):
        pass
    
    def add(self):
        pass
    
    def dep(self):
        pass
    
    def dep_chain(self):
        pass
    
    def dfs(self):
        pass
    
    def get(self):
        'Retrieve the pattern stored for a key.\n\n        key (unicode or int): The key to retrieve.\n        RETURNS (tuple): The rule, as an (on_match, patterns) tuple.\n        '
        pass
    
    def get_node_operator_map(self):
        pass
    
    def gov(self):
        pass
    
    def gov_chain(self):
        pass
    
    def has_key(self):
        'Check whether the matcher has a rule with a given key.\n\n        key (string or int): The key to check.\n        RETURNS (bool): Whether the matcher has the rule.\n        '
        pass
    
    def imm_left_sib(self):
        pass
    
    def imm_precede(self):
        pass
    
    def imm_right_sib(self):
        pass
    
    def left_sib(self):
        pass
    
    def retrieve_tree(self):
        pass
    
    def right_sib(self):
        pass
    
    @property
    def token_matcher(self):
        pass
    
    def validateInput(self):
        pass
    
    @property
    def vocab(self):
        pass
    

def Errors():
    '[__doc__] None'
    pass

INDEX_HEAD = 1
INDEX_RELOP = 0
__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/spacy/matcher/dependencymatcher.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'spacy.matcher.dependencymatcher'
__package__ = 'spacy.matcher'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def unpickle_matcher():
    pass

