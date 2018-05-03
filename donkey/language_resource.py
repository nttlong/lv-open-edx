class resources():
    request=None
    def __init__(self,request):
        self.request=request
    def get_global_res(self,key):
        return key
    def get_abs_url(self):
        request=self.request
        __root_url__ = None

        if request.get_full_path() == "/":
            __root_url__ = request.build_absolute_uri()
        else:
            __root_url__ = request.build_absolute_uri().replace(
                request.get_full_path(), "")
        if __root_url__[__root_url__.__len__() - 1] == "/":
            __root_url__ = __root_url__[0:__root_url__.__len__() - 1]
        return __root_url__
