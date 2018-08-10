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
        # if request.user.is_anonymous() or not request.user.is_superuser or not request.user.is_active:
        #     return redirect(request.get_abs_url()+"/login?next=/"+request.get_app_host())

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
@quicky.view.template("login.html")
@csrf_exempt
def login(request):
    if request.POST.keys().__len__()>0:
        username = request.POST.get("username","")
        password = request.POST.get("password", "")
        try:
            from django.contrib.auth.models import User
            from django.contrib.auth import authenticate, login
            from django.shortcuts import redirect

            user = authenticate(username=username, password=password)
            is_not_ok=user == None or user.is_superuser == False or user.is_active == False

            if is_not_ok:
                return request.render({
                    "next": request.GET("next",request.get_app_url("")),
                    "username": request.POST.get("username", ""),
                    "password": request.POST.get("password", ""),
                    "message": request.get_app_res("Login fail")

                })
            else:
                login(request, user)
                return redirect(request.GET.get("next",request.get_app_url("")))


        except Exception as ex:
            return request.render({
                "next": request.GET["next"],
                "username": request.POST.get("username", ""),
                "password": request.POST.get("password", ""),
                "message":request.get_app_res("Login fail")

            })


    return request.render({
        "next":request.GET["next"],
        "username":request.POST.get("username",""),
        "password": request.POST.get("password", ""),

    })
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