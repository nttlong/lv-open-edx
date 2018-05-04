import quicky
import sql_models
def get_list(param):
    session = quicky.sql_db.begin_session(param.app.settings.SQL_DB_CONFIG)
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
