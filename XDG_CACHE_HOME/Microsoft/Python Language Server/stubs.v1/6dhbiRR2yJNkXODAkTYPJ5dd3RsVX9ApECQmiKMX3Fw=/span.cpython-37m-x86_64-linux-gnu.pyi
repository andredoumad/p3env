import builtins as _mod_builtins
import collections as _mod_collections
import spacy.tokens.underscore as _mod_spacy_tokens_underscore

def Errors():
    '[__doc__] None'
    pass

class Span(_mod_builtins.object):
    'A slice from a Doc object.\n\n    DOCS: https://spacy.io/api/span\n    '
    @property
    def _(self):
        'Custom extension attributes registered via `set_extension`.'
        pass
    
    __class__ = Span
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, index):
        'Get a `Token` or a `Span` object\n\n        i (int or tuple): The index of the token within the span, or slice of\n            the span to get.\n        RETURNS (Token or Span): The token at `span[i]`.\n\n        DOCS: https://spacy.io/api/span#getitem\n        '
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        'A slice from a Doc object.\n\n    DOCS: https://spacy.io/api/span\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Iterate over `Token` objects.\n\n        YIELDS (Token): A `Token` object.\n\n        DOCS: https://spacy.io/api/span#iter\n        '
        return Span()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Get the number of tokens in the span.\n\n        RETURNS (int): The number of tokens in the span.\n\n        DOCS: https://spacy.io/api/span#len\n        '
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _recalculate_indices(self):
        pass
    
    @property
    def _vector(self):
        pass
    
    @property
    def _vector_norm(self):
        pass
    
    def as_doc(self):
        "Create a `Doc` object with a copy of the `Span`'s data.\n\n        RETURNS (Doc): The `Doc` copy of the span.\n\n        DOCS: https://spacy.io/api/span#as_doc\n        "
        pass
    
    @property
    def conjuncts(self):
        "Tokens that are conjoined to the span's root.\n\n        RETURNS (tuple): A tuple of Token objects.\n\n        DOCS: https://spacy.io/api/span#lefts\n        "
        pass
    
    @property
    def doc(self):
        pass
    
    @property
    def end(self):
        pass
    
    @property
    def end_char(self):
        pass
    
    @property
    def ent_id(self):
        'RETURNS (uint64): The entity ID.'
        pass
    
    @property
    def ent_id_(self):
        'RETURNS (unicode): The (string) entity ID.'
        pass
    
    @property
    def ents(self):
        'The named entities in the span. Returns a tuple of named entity\n        `Span` objects, if the entity recognizer has been applied.\n\n        RETURNS (tuple): Entities in the span, one `Span` per entity.\n\n        DOCS: https://spacy.io/api/span#ents\n        '
        pass
    
    @classmethod
    def get_extension(cls):
        'Look up a previously registered extension by name.\n\n        name (unicode): Name of the extension.\n        RETURNS (tuple): A `(default, method, getter, setter)` tuple.\n\n        DOCS: https://spacy.io/api/span#get_extension\n        '
        pass
    
    def get_lca_matrix(self):
        'Calculates a matrix of Lowest Common Ancestors (LCA) for a given\n        `Span`, where LCA[i, j] is the index of the lowest common ancestor among\n        the tokens span[i] and span[j]. If they have no common ancestor within\n        the span, LCA[i, j] will be -1.\n\n        RETURNS (np.array[ndim=2, dtype=numpy.int32]): LCA matrix with shape\n            (n, n), where n = len(self).\n\n        DOCS: https://spacy.io/api/span#get_lca_matrix\n        '
        pass
    
    @classmethod
    def has_extension(cls):
        'Check whether an extension has been registered.\n\n        name (unicode): Name of the extension.\n        RETURNS (bool): Whether the extension has been registered.\n\n        DOCS: https://spacy.io/api/span#has_extension\n        '
        pass
    
    @property
    def has_vector(self):
        'A boolean value indicating whether a word vector is associated with\n        the object.\n\n        RETURNS (bool): Whether a word vector is associated with the object.\n\n        DOCS: https://spacy.io/api/span#has_vector\n        '
        pass
    
    @property
    def label(self):
        pass
    
    @property
    def label_(self):
        "RETURNS (unicode): The span's label."
        pass
    
    @property
    def lefts(self):
        'Tokens that are to the left of the span, whose head is within the\n        `Span`.\n\n        YIELDS (Token):A left-child of a token of the span.\n\n        DOCS: https://spacy.io/api/span#lefts\n        '
        pass
    
    @property
    def lemma_(self):
        "RETURNS (unicode): The span's lemma."
        pass
    
    @property
    def lower_(self):
        'Deprecated. Use `Span.text.lower()` instead.'
        pass
    
    def merge(self):
        'Retokenize the document, such that the span is merged into a single\n        token.\n\n        **attributes: Attributes to assign to the merged token. By default,\n            attributes are inherited from the syntactic root token of the span.\n        RETURNS (Token): The newly merged token.\n        '
        pass
    
    @property
    def n_lefts(self):
        'The number of tokens that are to the left of the span, whose\n        heads are within the span.\n\n        RETURNS (int): The number of leftward immediate children of the\n            span, in the syntactic dependency parse.\n\n        DOCS: https://spacy.io/api/span#n_lefts\n        '
        pass
    
    @property
    def n_rights(self):
        'The number of tokens that are to the right of the span, whose\n        heads are within the span.\n\n        RETURNS (int): The number of rightward immediate children of the\n            span, in the syntactic dependency parse.\n\n        DOCS: https://spacy.io/api/span#n_rights\n        '
        pass
    
    @property
    def noun_chunks(self):
        'Yields base noun-phrase `Span` objects, if the document has been\n        syntactically parsed. A base noun phrase, or "NP chunk", is a noun\n        phrase that does not permit other NPs to be nested within it – so no\n        NP-level coordination, no prepositional phrases, and no relative\n        clauses.\n\n        YIELDS (Span): Base noun-phrase `Span` objects.\n\n        DOCS: https://spacy.io/api/span#noun_chunks\n        '
        pass
    
    @property
    def orth_(self):
        "Verbatim text content (identical to `Span.text`). Exists mostly for\n        consistency with other attributes.\n\n        RETURNS (unicode): The span's text."
        pass
    
    @classmethod
    def remove_extension(cls):
        'Remove a previously registered extension.\n\n        name (unicode): Name of the extension.\n        RETURNS (tuple): A `(default, method, getter, setter)` tuple of the\n            removed extension.\n\n        DOCS: https://spacy.io/api/span#remove_extension\n        '
        pass
    
    @property
    def rights(self):
        'Tokens that are to the right of the Span, whose head is within the\n        `Span`.\n\n        YIELDS (Token): A right-child of a token of the span.\n\n        DOCS: https://spacy.io/api/span#rights\n        '
        pass
    
    @property
    def root(self):
        'The token with the shortest path to the root of the\n        sentence (or the root itself). If multiple tokens are equally\n        high in the tree, the first token is taken.\n\n        RETURNS (Token): The root token.\n\n        DOCS: https://spacy.io/api/span#root\n        '
        pass
    
    @property
    def sent(self):
        'RETURNS (Span): The sentence span that the span is a part of.'
        pass
    
    @property
    def sentiment(self):
        'RETURNS (float): A scalar value indicating the positivity or\n            negativity of the span.\n        '
        pass
    
    @classmethod
    def set_extension(cls):
        'Define a custom attribute which becomes available as `Span._`.\n\n        name (unicode): Name of the attribute to set.\n        default: Optional default value of the attribute.\n        getter (callable): Optional getter function.\n        setter (callable): Optional setter function.\n        method (callable): Optional method for method extension.\n        force (bool): Force overwriting existing attribute.\n\n        DOCS: https://spacy.io/api/span#set_extension\n        USAGE: https://spacy.io/usage/processing-pipelines#custom-components-attributes\n        '
        pass
    
    def similarity(self):
        'Make a semantic similarity estimate. The default estimate is cosine\n        similarity using an average of word vectors.\n\n        other (object): The object to compare with. By default, accepts `Doc`,\n            `Span`, `Token` and `Lexeme` objects.\n        RETURNS (float): A scalar similarity score. Higher is more similar.\n\n        DOCS: https://spacy.io/api/span#similarity\n        '
        pass
    
    @property
    def start(self):
        pass
    
    @property
    def start_char(self):
        pass
    
    @property
    def string(self):
        'Deprecated: Use `Span.text_with_ws` instead.'
        pass
    
    @property
    def subtree(self):
        'Tokens within the span and tokens which descend from them.\n\n        YIELDS (Token): A token within the span, or a descendant from it.\n\n        DOCS: https://spacy.io/api/span#subtree\n        '
        pass
    
    @property
    def text(self):
        'RETURNS (unicode): The original verbatim text of the span.'
        pass
    
    @property
    def text_with_ws(self):
        'The text content of the span with a trailing whitespace character if\n        the last token has one.\n\n        RETURNS (unicode): The text content of the span (with trailing\n            whitespace).\n        '
        pass
    
    def to_array(self):
        'Given a list of M attribute IDs, export the tokens to a numpy\n        `ndarray` of shape `(N, M)`, where `N` is the length of the document.\n        The values will be 32-bit integers.\n\n        attr_ids (list[int]): A list of attribute ID ints.\n        RETURNS (numpy.ndarray[long, ndim=2]): A feature matrix, with one row\n            per word, and one column per attribute indicated in the input\n            `attr_ids`.\n        '
        pass
    
    @property
    def upper_(self):
        'Deprecated. Use `Span.text.upper()` instead.'
        pass
    
    @property
    def vector(self):
        "A real-valued meaning representation. Defaults to an average of the\n        token vectors.\n\n        RETURNS (numpy.ndarray[ndim=1, dtype='float32']): A 1D numpy array\n            representing the span's semantics.\n\n        DOCS: https://spacy.io/api/span#vector\n        "
        pass
    
    @property
    def vector_norm(self):
        "The L2 norm of the span's vector representation.\n\n        RETURNS (float): The L2 norm of the vector representation.\n\n        DOCS: https://spacy.io/api/span#vector_norm\n        "
        pass
    
    @property
    def vocab(self):
        "RETURNS (Vocab): The Span's Doc's vocab."
        pass
    

def TempErrors():
    '[__doc__] None'
    pass

Underscore = _mod_spacy_tokens_underscore.Underscore
def Warnings():
    '[__doc__] None'
    pass

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/spacy/tokens/span.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'spacy.tokens.span'
__package__ = 'spacy.tokens'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
basestring_ = _mod_builtins.str
defaultdict = _mod_collections.defaultdict
def deprecation_warning(message):
    pass

def get_array_module(_):
    pass

def get_ext_args(**kwargs):
    'Validate and convert arguments. Reused in Doc, Token and Span.'
    pass

def is_config(python2, python3, windows, linux, osx):
    "Check if a specific configuration of Python version and operating system\n    matches the user's setup. Mostly used to display targeted error messages.\n\n    python2 (bool): spaCy is executed with Python 2.x.\n    python3 (bool): spaCy is executed with Python 3.x.\n    windows (bool): spaCy is executed on Windows.\n    linux (bool): spaCy is executed on Linux.\n    osx (bool): spaCy is executed on OS X or macOS.\n    RETURNS (bool): Whether the configuration matches the user's platform.\n\n    DOCS: https://spacy.io/api/top-level#compat.is_config\n    "
    pass

def models_warning(message):
    pass

def normalize_slice(length, start, stop, step):
    pass

def user_warning(message):
    pass

