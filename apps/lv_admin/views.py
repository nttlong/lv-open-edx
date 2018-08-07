# -*- coding: utf-8 -*-
import quicky
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
app=quicky.applications.get_app_by_file(__file__)
import json
@quicky.view.template("index.html")
def index(request):
    try:
        from django.http.response import HttpResponseRedirect
        from django.shortcuts import redirect
        if request.user.is_anonymous() or not request.user.is_superuser or not request.user.is_active:
            return redirect(request.get_abs_url()+"/login?next=/"+request.get_app_host())

        return request.render(dict(
            menu_items=app.settings.menu_items
        ))
    except Exception as ex:
        return request.render(dict(
            menu_items=app.settings.menu_items
        ))
@quicky.view.template("dynamic.html")
def load_page(request,path):

    return request.render({
        "path": path.lower()
    })
@require_http_methods(["POST"])
@csrf_exempt
def api(request):
    from django.shortcuts import redirect
    if request.user.is_anonymous() or not request.user.is_superuser or not request.user.is_active:
        return redirect(request.get_abs_url()+"/login?next=/"+request.get_app_host())

    setattr(request,"app",app)
    ret_data=quicky.caller.call(request)
    return HttpResponse(ret_data)
def login(request):
    pass
@quicky.view.template("download_excel.html")
def download_excel(request,path):
    import importlib
    export_module=importlib.import_module(app.mdl.__name__+".{0}.{1}".format('excel_export',path))

    return export_module.do_export(request)
@quicky.view.template("download_excel_error.html")
def download_excel_error(request,id):
    import qexcel
    ret = qexcel.get_error(id)

    return ret