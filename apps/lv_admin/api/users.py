import quicky
import sql_models
from quicky import applications
app = applications.get_app_by_file(__file__)
def get_list(param):
    from sqlalchemy import or_, and_
    from django.conf import settings
    session = quicky.sql_db.begin_session(param.app.settings.get_db_config())
    total_items=0
    ret={}
    try:
        page_size=param.data.get("page_size",20)
        page_index=param.data.get("page_index",0)
        qr= session.query(sql_models.models.AuthUser)
        if param.data.get("search_text",None) != None:
            txt_search = param.data.get("search_text")
            qr = qr.filter(or_(
                sql_models.models.AuthUser.username.like("%"+txt_search+"%"),
                sql_models.models.AuthUser.email.like("%" + txt_search + "%"))
            )
        if param.data.get("filter",None) != None and param.data["filter"].keys().__len__()>0:
            fx_and =and_
            for x in param.data.get("filter",None).keys():
                qr = qr.filter(getattr(sql_models.models.AuthUser,x).like("%"+param.data["filter"][x]["filter"]+"%"))
            #     fx_and=fx_and(getattr(sql_models.models.AuthUser,x).like("%"+param.data["filter"][x]["filter"]+"%"))
            # qr=qr.filter(fx_and)


        total_items=qr.count()
        if param.data.get("sort",None)!= None:
            for x in param.data["sort"]:
                qr =qr.order_by(getattr(getattr(sql_models.models.AuthUser,x['colId']),x["sort"])())

        else:
             qr= qr.order_by(sql_models.models.AuthUser.username)

        items = list(qr.offset(page_size * page_index).limit(page_size))
        ret=dict(
            pageSize=page_size,
            pageIndex=page_index,
            totalItems=total_items,
            items=items
        )


        quicky.sql_db.end_session(session)
    except Exception as ex:
        quicky.sql_db.end_session(session)
        raise ex
    return ret
def import_excel(args):
    return {}