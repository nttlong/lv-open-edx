# -*- coding: utf-8 -*-
import quicky
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
@quicky.view.template("index.html")
def index(request):
    return request.render(dict(
        menu_items=[
            dict(
                caption="Phân quyền",
                items=[
                    dict(caption="Người dùng",
                         page="users")
                ]
            )
        ]
    ))
@quicky.view.template("dynamic.html")
def load_page(request,path):

    return request.render({
        "path": path.lower()
    })
@require_http_methods(["POST"])
@csrf_exempt
def api(request):
    # login_info=argo.get_settings().MEMBERSHIP_ENGINE.validate_session(request.session.session_key)
    # if login_info==None:
    #     return HttpResponse('401 Unauthorized', status=401)
    # if not login_info.user.isSysAdmin:
    #     return HttpResponse('401 Unauthorized', status=401)
    #
    # post_data=json.loads(request.body)
    #
    #
    # if not post_data.has_key("path"):
    #     raise Exception("Api post without using path")
    # path=post_data["path"]
    # view=post_data["view"]
    # if post_data["path"].split("/").__len__()!=2:
    #     raise Exception("'{0}' is invalid path, path must be */*")
    #
    # view_privileges=argo.get_settings().AUTHORIZATION_ENGINE.get_view_of_user(
    #     view_id=view,
    #     user_id=login_info.user.userId
    # )
    # if login_info.user.isSysAdmin:
    #     view_privileges={"is_public":True}
    # if view_privileges==None and not login_info.user.isSysAdmin:
    #     return HttpResponse('401 Unauthorized', status=401)
    #
    # module_path=path.split("/")[0]
    # method_path=path.split('/')[1]
    # mdl=None
    # try:
    #     mdl = importlib.import_module("hrm.bll."+module_path)
    # except Exception as ex:
    #     raise Exception("import '{0}' encountered '{1}'".format(module_path,ex.message))
    #
    # ret=None
    #
    # if mdl!=None:
    #     if not hasattr(mdl,method_path):
    #         raise (Exception("'{0}' was not found in '{1}'".format(method_path,"hrm.bll."+module_path)))
    #     try:
    #         if post_data.has_key("data"):
    #             ret=getattr(mdl,method_path)(
    #                 {
    #                     "privileges":view_privileges,
    #                     "data":post_data.get("data",{}),
    #                     "user":login_info.user,
    #                     "view":view
    #                 })
    #         else:
    #             ret = getattr(mdl, method_path)(
    #                 {
    #                     "privileges":view_privileges,
    #                     "user":login_info.user,
    #                     "view":view
    #                 })
    #
    #     except Exception as ex:
    #         raise Exception("Call  '{0}' in '{1}' encountered '{2}'".format(method_path, module_path, ex))
    # ret_data=argo.utilities.to_json(ret)
    return HttpResponse(ret_data)