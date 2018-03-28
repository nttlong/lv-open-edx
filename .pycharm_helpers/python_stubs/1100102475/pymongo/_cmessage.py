# encoding: utf-8
# module pymongo._cmessage
# from /usr/local/lib/python2.7/dist-packages/pymongo/_cmessage.so
# by generator 1.145
# no doc
# no imports

# functions

def _do_batched_insert(*args, **kwargs): # real signature unknown
    """ insert a batch of documents, splitting the batch as needed """
    pass

def _do_batched_write_command(*args, **kwargs): # real signature unknown
    """ execute a batch of insert, update, or delete commands """
    pass

def _get_more_message(*args, **kwargs): # real signature unknown
    """ create a get more message to be sent to MongoDB """
    pass

def _insert_message(*args, **kwargs): # real signature unknown
    """
    Create an insert message to be sent to MongoDB
    
    Note: As of PyMongo 2.6, this function is no longer used. It
    is being kept (with tests) for backwards compatibility with 3rd
    party libraries that may currently be using it, but will likely
    be removed in a future release.
    """
    pass

def _query_message(*args, **kwargs): # real signature unknown
    """ create a query message to be sent to MongoDB """
    pass

def _update_message(*args, **kwargs): # real signature unknown
    """ create an update message to be sent to MongoDB """
    pass

# no classes
