
def get_csrftoken(request):
    from django.core.context_processors import csrf
    if type(csrf(request)["csrf_token"]) is str:
        return csrf(request)["csrf_token"]
    else:
        return csrf(request)["csrf_token"].encode()