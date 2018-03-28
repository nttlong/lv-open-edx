# encoding: utf-8
# module meliae._intset
# from /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/meliae/_intset.so
# by generator 1.145
"""
A structure for handling a set of pure integers.

(Such as a set of python object ids.)
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# no functions
# classes

class IntSet(object):
    """
    Keep a set of integer objects.
    
        This is slightly more efficient than a PySet because we don't allow
        arbitrary types.
    """
    def add(self, *args, **kwargs): # real signature unknown
        """ Add a new entry to the set. """
        pass

    def _peek_array(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    _has_singleton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class IDSet(IntSet):
    """
    Track a set of object ids (addresses).
    
        This only differs from IntSet in how the integers are hashed. Object
        addresses tend to be aligned on 16-byte boundaries (occasionally 8-byte,
        and even more rarely on 4-byte), as such the standard hash lookup has more
        collisions than desired.
    
        Also, addresses are considered to be unsigned longs by python, but
        Py_ssize_t is a signed long. Just treating it normally causes us to get a
        value overflow on 32-bits if the highest bit is set.
    """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__test__ = {}

