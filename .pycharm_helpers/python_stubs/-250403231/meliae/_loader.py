# encoding: utf-8
# module meliae._loader
# from /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/meliae/_loader.so
# by generator 1.145
""" Routines and objects for loading dump files. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import meliae.warn as warn # /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/meliae/warn.pyc
import gc as gc # <module 'gc' (built-in)>

# functions

def _all_sort_key(*args, **kwargs): # real signature unknown
    pass

def _MemObjectProxy_from_args(*args, **kwargs): # real signature unknown
    """
    Create a standalone _MemObjectProxy instance.
    
        Note that things like '__getitem__' won't work, as they query the
        collection for the actual data.
    """
    pass

# classes

class MemObjectCollection(object):
    """ Track a bunch of _MemObject instances. """
    def add(self, *args, **kwargs): # real signature unknown
        """ Add a new MemObject to this collection. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        """ Iterate over (key, value) tuples. """
        pass

    def iteritems(self, *args, **kwargs): # real signature unknown
        pass

    def iterkeys(self, *args, **kwargs): # real signature unknown
        pass

    def itervalues(self, *args, **kwargs): # real signature unknown
        """ Return an iterable of values stored in this map. """
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        pass

    def _test_lookup(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    _active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _filled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _table_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class _MemObjectProxy(object):
    """
    The standard interface for understanding memory consumption.
    
        MemObjectCollection stores the data as a fairly efficient table, without
        the overhead of having a regular python object for every data point.
        However, the rest of python code needs to interact with a real python
        object, so we generate these on-the-fly.
    
        Most attributes are properties, which thunk over to the actual data table
        entry.
    
        :ivar address: The address in memory of the original object. This is used
            as the 'handle' to this object.
        :ivar type_str: The type of this object
        :ivar size: The number of bytes consumed for just this object. So for a
            dict, this would be the basic_size + the size of the allocated array to
            store the reference pointers
        :ivar children: A list of items referenced from this object
        :ivar num_refs: Count of references, you can also use len()
        :ivar value: A PyObject representing the Value for this object. (For
            strings, it is the first 100 bytes, it may be None if we have no value,
            or it may be an integer, etc.) This is also where the 'name' is stored
            for objects like 'module'.
        :ivar
    """
    def all(self, *args, **kwargs): # real signature unknown
        """
        Retrieve a list of all the referenced items matching type_str.
        
                :param type_str: Children must match this type string.
                :param excluding: See iter_recursive_refs
                :return: A list of all entries, sorted with the largest entries first.
        """
        pass

    def compute_total_size(self, *args, **kwargs): # real signature unknown
        """
        Compute the number of bytes of this and all referenced objects.
        
                This layers on top of iter_recursive_refs to give just the interesting
                bits.
        
                :return: total_size, this will also be set on self.
        """
        pass

    def iter_recursive_refs(self, *args, **kwargs): # real signature unknown
        """
        Find all objects referenced from this one (including self).
        
                Self will always be the first object returned, in case you want to
                exclude it (though it can be excluded in the excluding list). This is
                done because it is cumbersome to add it back in, but easy to exclude.
        
                :param excluding: This can be any iterable of addresses. We will not
                    walk to anything in this list (including self).
                :return: Iterator over all objects that can be reached.
        """
        pass

    def refs_as_dict(self, *args, **kwargs): # real signature unknown
        """
        Expand the ref list considering it to be a 'dict' structure.
        
                Often we have dicts that point to simple strings and ints, etc. This
                tries to expand that as much as possible.
        """
        pass

    def to_json(self, *args, **kwargs): # real signature unknown
        """ Convert this back into json. """
        pass

    def _intern_from_cache(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier for the tracked object."""

    c = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of children objects as objects (not references)."""

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of objects referenced by this object."""

    num_parents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the parents list."""

    num_referrers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the parents list."""

    num_refs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    p = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of parent objects as objects (not references)."""

    parents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of objects that reference this object.

        Original set to None, can be computed on demand.
        """

    referrers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Objects which refer to this object.

        Deprecated, use .parents instead.
        """

    ref_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of objects referenced by this object.

        Deprecated, use .children instead.
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes allocated for this object."""

    total_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Mean to hold the size of this plus size of all referenced objects."""

    type_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of this object."""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value for this object (for strings and ints)"""



class _MOCValueIterator(object):
    """ A simple iterator over the values in a MOC. """
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass


class _MOPReferencedIterator(object):
    """ Iterate over all the children referenced from this object. """
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__test__ = {}

