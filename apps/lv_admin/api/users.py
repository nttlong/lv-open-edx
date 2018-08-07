import quicky
import sql_models
from quicky import applications
app = applications.get_app_by_file(__file__)
def get_list(param):
    from django.conf import settings
    session = quicky.sql_db.begin_session(param.app.settings.get_db_config())
    total_items=0
    ret={}
    try:
        page_size=param.data.get("page_size",20)
        page_index=param.data.get("page_index",0)
        total_items=session.query(sql_models.models.AuthUser).count()
        items=list(session.query(sql_models.models.AuthUser).order_by(sql_models.models.AuthUser.username).offset(page_size*page_index).limit(page_size))
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