# encoding: utf-8
# module meliae._scanner
# from /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/meliae/_scanner.so
# by generator 1.145
""" The core routines for scanning python references and dumping memory info. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# Variables with simple values

_gc_head_size = 32

_unicode_size = 4

_word_size = 8

# functions

def add_special_size(*args, **kwargs): # real signature unknown
    """
    Special case a given object size.
    
        This is only meant to be used for objects we don't already handle or which
        don't implement __sizeof__ (those are checked before this check happens).
    
        This is meant for things like zlib.Compress which allocates a lot of
        internal buffers, which are not easily accessible (but can be
        approximated).  The gc header should not be included in this size, it will
        be added at runtime.
    
        Setting the value to None will remove the value.
    
        (We only distinguish size_of_32 from size_of_64 for the implementer's
        benefit, since sizeof() is not generally accessible from Python.)
    
        :param tp_name: The type string we care about (such as 'zlib.Compress').
            This will be matched against object->type->tp_name.
        :param size_of_32: Called when _word_size == 32-bits
        :param size_of_64: Called when _word_size == 64-bits
        :return: None
    """
    pass

def dump_object_info(*args, **kwargs): # real signature unknown
    """
    Dump the object information to the given output.
    
        :param out: Either a File object, or a callable.
            If a File object, we will write bytes to the underlying FILE*
            Otherwise, we will call(str) with bytes as we build up the state of the
            object. Note that a single call will not be a complete description, but
            potentially a single character of the final formatted string.
        :param obj: The object to inspect
        :param nodump: If supplied, this is a set() of objects that we want to
            exclude from the dump file.
        :param recurse_depth: 0 to only dump the supplied object
           1 to dump the object and immediate neighbors that would not otherwise be
           referenced (such as strings).
           2 dump everything we find and continue recursing
    """
    pass

def get_referents(): # real signature unknown; restored from __doc__
    """
    Similar to gc.get_referents()
    
        The main different is that gc.get_referents() only includes items that are
        in the garbage collector. However, we want anything referred to by
        tp_traverse.
    """
    pass

def size_of(*args, **kwargs): # real signature unknown
    """
    Compute the size of the object.
    
        This is the actual malloc() size for this object, so for dicts it is the
        size of the dict object, plus the size of the array of references, but
        *not* the size of each individual referenced object.
    
        :param obj: The object to measure
        :return: An integer of the number of bytes used by this object.
    """
    pass

def _zlib_size_of_32(*args, **kwargs): # real signature unknown
    """ Return a __sizeof__ for a zlib object. """
    pass

def _zlib_size_of_64(*args, **kwargs): # real signature unknown
    """ Return a __sizeof__ for a zlib object. """
    pass

# no classes
# variables with complex values

__test__ = {}

