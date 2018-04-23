from . import extens
from . import applications
def template_uri(fn):
    def layer(*args, **kwargs):
        def repl(f):
            return fn(f,*args, **kwargs)
        return repl
    return layer
@template_uri
def template(fn,*_path,**kwargs):
    if _path.__len__()==1:
        _path=_path[00]
    if _path.__len__()==0:
        _path=kwargs


    app=applications.get_app_by_file(fn.func_code.co_filename)
    def exec_request(request, **kwargs):
        extens.apply(request,_path,app)
        return fn(request, **kwargs)
    return exec_request