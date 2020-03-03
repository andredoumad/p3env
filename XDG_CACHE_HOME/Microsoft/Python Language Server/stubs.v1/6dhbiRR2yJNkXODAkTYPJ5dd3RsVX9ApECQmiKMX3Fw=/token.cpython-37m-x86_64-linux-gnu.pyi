import builtins as _mod_builtins
import spacy.tokens.underscore as _mod_spacy_tokens_underscore

def Errors():
    '[__doc__] None'
    pass

class Token(_mod_builtins.object):
    'An individual token – i.e. a word, punctuation symbol, whitespace,\n    etc.\n\n    DOCS: https://spacy.io/api/token\n    '
    @property
    def _(self):
        'Custom extension attributes registered via `set_extension`.'
        pass
    
    def __bytes__(self):
        pass
    
    __class__ = Token
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        'An individual token – i.e. a word, punctuation symbol, whitespace,\n    etc.\n\n    DOCS: https://spacy.io/api/token\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'The number of unicode characters in the token, i.e. `token.text`.\n\n        RETURNS (int): The number of unicode characters in the token.\n\n        DOCS: https://spacy.io/api/token#len\n        '
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
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    @property
    def ancestors(self):
        "A sequence of this token's syntactic ancestors.\n\n        YIELDS (Token): A sequence of ancestor tokens such that\n            `ancestor.is_ancestor(self)`.\n\n        DOCS: https://spacy.io/api/token#ancestors\n        "
        pass
    
    def check_flag(self):
        'Check the value of a boolean flag.\n\n        flag_id (int): The ID of the flag attribute.\n        RETURNS (bool): Whether the flag is set.\n\n        DOCS: https://spacy.io/api/token#check_flag\n        '
        pass
    
    @property
    def children(self):
        "A sequence of the token's immediate syntactic children.\n\n        YIELDS (Token): A child token such that `child.head==self`.\n\n        DOCS: https://spacy.io/api/token#children\n        "
        pass
    
    @property
    def cluster(self):
        'RETURNS (int): Brown cluster ID.'
        pass
    
    @property
    def conjuncts(self):
        'A sequence of coordinated tokens, including the token itself.\n\n        RETURNS (tuple): The coordinated tokens.\n\n        DOCS: https://spacy.io/api/token#conjuncts\n        '
        pass
    
    @property
    def dep(self):
        'RETURNS (uint64): ID of syntactic dependency label.'
        pass
    
    @property
    def dep_(self):
        'RETURNS (unicode): The syntactic dependency label.'
        pass
    
    @property
    def doc(self):
        pass
    
    @property
    def ent_id(self):
        'RETURNS (uint64): ID of the entity the token is an instance of,\n            if any.\n        '
        pass
    
    @property
    def ent_id_(self):
        'RETURNS (unicode): ID of the entity the token is an instance of,\n            if any.\n        '
        pass
    
    @property
    def ent_iob(self):
        'IOB code of named entity tag. `1="I", 2="O", 3="B"`. 0 means no tag\n        is assigned.\n\n        RETURNS (uint64): IOB code of named entity tag.\n        '
        pass
    
    @property
    def ent_iob_(self):
        'IOB code of named entity tag. "B" means the token begins an entity,\n        "I" means it is inside an entity, "O" means it is outside an entity,\n        and "" means no entity tag is set.\n\n        RETURNS (unicode): IOB code of named entity tag.\n        '
        pass
    
    @property
    def ent_type(self):
        'RETURNS (uint64): Named entity type.'
        pass
    
    @property
    def ent_type_(self):
        'RETURNS (unicode): Named entity type.'
        pass
    
    @classmethod
    def get_extension(cls):
        'Look up a previously registered extension by name.\n\n        name (unicode): Name of the extension.\n        RETURNS (tuple): A `(default, method, getter, setter)` tuple.\n\n        DOCS: https://spacy.io/api/token#get_extension\n        '
        pass
    
    @classmethod
    def has_extension(cls):
        'Check whether an extension has been registered.\n\n        name (unicode): Name of the extension.\n        RETURNS (bool): Whether the extension has been registered.\n\n        DOCS: https://spacy.io/api/token#has_extension\n        '
        pass
    
    @property
    def has_vector(self):
        'A boolean value indicating whether a word vector is associated with\n        the object.\n\n        RETURNS (bool): Whether a word vector is associated with the object.\n\n        DOCS: https://spacy.io/api/token#has_vector\n        '
        pass
    
    @property
    def head(self):
        'The syntactic parent, or "governor", of this token.\n\n        RETURNS (Token): The token predicted by the parser to be the head of\n            the current token.\n        '
        pass
    
    @property
    def i(self):
        pass
    
    @property
    def idx(self):
        'RETURNS (int): The character offset of the token within the parent\n            document.\n        '
        pass
    
    @property
    def is_alpha(self):
        'RETURNS (bool): Whether the token consists of alpha characters.\n            Equivalent to `token.text.isalpha()`.\n        '
        pass
    
    def is_ancestor(self):
        'Check whether this token is a parent, grandparent, etc. of another\n        in the dependency tree.\n\n        descendant (Token): Another token.\n        RETURNS (bool): Whether this token is the ancestor of the descendant.\n\n        DOCS: https://spacy.io/api/token#is_ancestor\n        '
        pass
    
    @property
    def is_ascii(self):
        'RETURNS (bool): Whether the token consists of ASCII characters.\n            Equivalent to `[any(ord(c) >= 128 for c in token.text)]`.\n        '
        pass
    
    @property
    def is_bracket(self):
        'RETURNS (bool): Whether the token is a bracket.'
        pass
    
    @property
    def is_currency(self):
        'RETURNS (bool): Whether the token is a currency symbol.'
        pass
    
    @property
    def is_digit(self):
        'RETURNS (bool): Whether the token consists of digits. Equivalent to\n            `token.text.isdigit()`.\n        '
        pass
    
    @property
    def is_left_punct(self):
        'RETURNS (bool): Whether the token is a left punctuation mark.'
        pass
    
    @property
    def is_lower(self):
        'RETURNS (bool): Whether the token is in lowercase. Equivalent to\n            `token.text.islower()`.\n        '
        pass
    
    @property
    def is_oov(self):
        'RETURNS (bool): Whether the token is out-of-vocabulary.'
        pass
    
    @property
    def is_punct(self):
        'RETURNS (bool): Whether the token is punctuation.'
        pass
    
    @property
    def is_quote(self):
        'RETURNS (bool): Whether the token is a quotation mark.'
        pass
    
    @property
    def is_right_punct(self):
        'RETURNS (bool): Whether the token is a right punctuation mark.'
        pass
    
    @property
    def is_sent_start(self):
        'A boolean value indicating whether the token starts a sentence.\n        `None` if unknown. Defaults to `True` for the first token in the `Doc`.\n\n        RETURNS (bool / None): Whether the token starts a sentence.\n            None if unknown.\n\n        DOCS: https://spacy.io/api/token#is_sent_start\n        '
        pass
    
    @property
    def is_space(self):
        'RETURNS (bool): Whether the token consists of whitespace characters.\n            Equivalent to `token.text.isspace()`.\n        '
        pass
    
    @property
    def is_stop(self):
        'RETURNS (bool): Whether the token is a stop word, i.e. part of a\n            "stop list" defined by the language data.\n        '
        pass
    
    @property
    def is_title(self):
        'RETURNS (bool): Whether the token is in titlecase. Equivalent to\n            `token.text.istitle()`.\n        '
        pass
    
    @property
    def is_upper(self):
        'RETURNS (bool): Whether the token is in uppercase. Equivalent to\n            `token.text.isupper()`\n        '
        pass
    
    @property
    def lang(self):
        "RETURNS (uint64): ID of the language of the parent document's\n            vocabulary.\n        "
        pass
    
    @property
    def lang_(self):
        "RETURNS (unicode): Language of the parent document's vocabulary,\n            e.g. 'en'.\n        "
        pass
    
    @property
    def left_edge(self):
        "The leftmost token of this token's syntactic descendents.\n\n        RETURNS (Token): The first token such that `self.is_ancestor(token)`.\n        "
        pass
    
    @property
    def lefts(self):
        'The leftward immediate children of the word, in the syntactic\n        dependency parse.\n\n        YIELDS (Token): A left-child of the token.\n\n        DOCS: https://spacy.io/api/token#lefts\n        '
        pass
    
    @property
    def lemma(self):
        'RETURNS (uint64): ID of the base form of the word, with no\n            inflectional suffixes.\n        '
        pass
    
    @property
    def lemma_(self):
        'RETURNS (unicode): The token lemma, i.e. the base form of the word,\n            with no inflectional suffixes.\n        '
        pass
    
    @property
    def lex_id(self):
        "RETURNS (int): Sequential ID of the token's lexical type."
        pass
    
    @property
    def like_email(self):
        'RETURNS (bool): Whether the token resembles an email address.'
        pass
    
    @property
    def like_num(self):
        'RETURNS (bool): Whether the token resembles a number, e.g. "10.9",\n            "10", "ten", etc.\n        '
        pass
    
    @property
    def like_url(self):
        'RETURNS (bool): Whether the token resembles a URL.'
        pass
    
    @property
    def lower(self):
        'RETURNS (uint64): ID of the lowercase token text.'
        pass
    
    @property
    def lower_(self):
        'RETURNS (unicode): The lowercase token text. Equivalent to\n            `Token.text.lower()`.\n        '
        pass
    
    @property
    def n_lefts(self):
        'The number of leftward immediate children of the word, in the\n        syntactic dependency parse.\n\n        RETURNS (int): The number of leftward immediate children of the\n            word, in the syntactic dependency parse.\n\n        DOCS: https://spacy.io/api/token#n_lefts\n        '
        pass
    
    @property
    def n_rights(self):
        'The number of rightward immediate children of the word, in the\n        syntactic dependency parse.\n\n        RETURNS (int): The number of rightward immediate children of the\n            word, in the syntactic dependency parse.\n\n        DOCS: https://spacy.io/api/token#n_rights\n        '
        pass
    
    def nbor(self):
        'Get a neighboring token.\n\n        i (int): The relative position of the token to get. Defaults to 1.\n        RETURNS (Token): The token at position `self.doc[self.i+i]`.\n\n        DOCS: https://spacy.io/api/token#nbor\n        '
        pass
    
    @property
    def norm(self):
        "RETURNS (uint64): ID of the token's norm, i.e. a normalised form of\n            the token text. Usually set in the language's tokenizer exceptions\n            or norm exceptions.\n        "
        pass
    
    @property
    def norm_(self):
        "RETURNS (unicode): The token's norm, i.e. a normalised form of the\n            token text. Usually set in the language's tokenizer exceptions or\n            norm exceptions.\n        "
        pass
    
    @property
    def orth(self):
        'RETURNS (uint64): ID of the verbatim text content.'
        pass
    
    @property
    def orth_(self):
        'RETURNS (unicode): Verbatim text content (identical to\n            `Token.text`). Exists mostly for consistency with the other\n            attributes.\n        '
        pass
    
    @property
    def pos(self):
        'RETURNS (uint64): ID of coarse-grained part-of-speech tag.'
        pass
    
    @property
    def pos_(self):
        'RETURNS (unicode): Coarse-grained part-of-speech tag.'
        pass
    
    @property
    def prefix(self):
        'RETURNS (uint64): ID of a length-N substring from the start of the\n            token. Defaults to `N=1`.\n        '
        pass
    
    @property
    def prefix_(self):
        'RETURNS (unicode): A length-N substring from the start of the token.\n            Defaults to `N=1`.\n        '
        pass
    
    @property
    def prob(self):
        'RETURNS (float): Smoothed log probability estimate of token type.'
        pass
    
    @property
    def rank(self):
        "RETURNS (int): Sequential ID of the token's lexical type, used to\n        index into tables, e.g. for word vectors."
        pass
    
    @classmethod
    def remove_extension(cls):
        'Remove a previously registered extension.\n\n        name (unicode): Name of the extension.\n        RETURNS (tuple): A `(default, method, getter, setter)` tuple of the\n            removed extension.\n\n        DOCS: https://spacy.io/api/token#remove_extension\n        '
        pass
    
    @property
    def right_edge(self):
        "The rightmost token of this token's syntactic descendents.\n\n        RETURNS (Token): The last token such that `self.is_ancestor(token)`.\n        "
        pass
    
    @property
    def rights(self):
        'The rightward immediate children of the word, in the syntactic\n        dependency parse.\n\n        YIELDS (Token): A right-child of the token.\n\n        DOCS: https://spacy.io/api/token#rights\n        '
        pass
    
    @property
    def sent(self):
        'RETURNS (Span): The sentence span that the token is a part of.'
        pass
    
    @property
    def sent_start(self):
        pass
    
    @property
    def sentiment(self):
        'RETURNS (float): A scalar value indicating the positivity or\n            negativity of the token.'
        pass
    
    @classmethod
    def set_extension(cls):
        'Define a custom attribute which becomes available as `Token._`.\n\n        name (unicode): Name of the attribute to set.\n        default: Optional default value of the attribute.\n        getter (callable): Optional getter function.\n        setter (callable): Optional setter function.\n        method (callable): Optional method for method extension.\n        force (bool): Force overwriting existing attribute.\n\n        DOCS: https://spacy.io/api/token#set_extension\n        USAGE: https://spacy.io/usage/processing-pipelines#custom-components-attributes\n        '
        pass
    
    @property
    def shape(self):
        'RETURNS (uint64): ID of the token\'s shape, a transform of the\n            tokens\'s string, to show orthographic features (e.g. "Xxxx", "dd").\n        '
        pass
    
    @property
    def shape_(self):
        'RETURNS (unicode): Transform of the tokens\'s string, to show\n            orthographic features. For example, "Xxxx" or "dd".\n        '
        pass
    
    def similarity(self):
        'Make a semantic similarity estimate. The default estimate is cosine\n        similarity using an average of word vectors.\n\n        other (object): The object to compare with. By default, accepts `Doc`,\n            `Span`, `Token` and `Lexeme` objects.\n        RETURNS (float): A scalar similarity score. Higher is more similar.\n\n        DOCS: https://spacy.io/api/token#similarity\n        '
        pass
    
    @property
    def string(self):
        'Deprecated: Use Token.text_with_ws instead.'
        pass
    
    @property
    def subtree(self):
        "A sequence containing the token and all the token's syntactic\n        descendants.\n\n        YIELDS (Token): A descendent token such that\n            `self.is_ancestor(descendent) or token == self`.\n\n        DOCS: https://spacy.io/api/token#subtree\n        "
        pass
    
    @property
    def suffix(self):
        'RETURNS (uint64): ID of a length-N substring from the end of the\n            token. Defaults to `N=3`.\n        '
        pass
    
    @property
    def suffix_(self):
        'RETURNS (unicode): A length-N substring from the end of the token.\n            Defaults to `N=3`.\n        '
        pass
    
    @property
    def tag(self):
        'RETURNS (uint64): ID of fine-grained part-of-speech tag.'
        pass
    
    @property
    def tag_(self):
        'RETURNS (unicode): Fine-grained part-of-speech tag.'
        pass
    
    @property
    def text(self):
        'RETURNS (unicode): The original verbatim text of the token.'
        pass
    
    @property
    def text_with_ws(self):
        'RETURNS (unicode): The text content of the span (with trailing\n            whitespace).\n        '
        pass
    
    @property
    def vector(self):
        "A real-valued meaning representation.\n\n        RETURNS (numpy.ndarray[ndim=1, dtype='float32']): A 1D numpy array\n            representing the token's semantics.\n\n        DOCS: https://spacy.io/api/token#vector\n        "
        pass
    
    @property
    def vector_norm(self):
        "The L2 norm of the token's vector representation.\n\n        RETURNS (float): The L2 norm of the vector representation.\n\n        DOCS: https://spacy.io/api/token#vector_norm\n        "
        pass
    
    @property
    def vocab(self):
        pass
    
    @property
    def whitespace_(self):
        'RETURNS (unicode): The trailing whitespace character, if present.'
        pass
    

Underscore = _mod_spacy_tokens_underscore.Underscore
def Warnings():
    '[__doc__] None'
    pass

__builtins__ = {}
__doc__ = None
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/spacy/tokens/token.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'spacy.tokens.token'
__package__ = 'spacy.tokens'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
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

def user_warning(message):
    pass

