import quicky
import sql_models
def do_export(request):
    from django.http import HttpResponse
    import openpyxl
    session = quicky.sql_db.begin_session(request.get_app().settings.SQL_DB_CONFIG)
    total_items = 0
    ret = {}
    try:

        total_items = session.query(sql_models.models.AuthUser).count()
        items = list(session.query(sql_models.models.AuthUser))
        quicky.sql_db.end_session(session)
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        header_attr=["username","email","first_name","last_name","is_active","is_staff","is_superuser"]
        for x in header_attr:
            col_index=header_attr.index(x)+1
            ws.cell(1, col_index).value = x
        row_index=2
        for row in items:
            for x in header_attr:
                col_index = header_attr.index(x) + 1
                ws.cell(row_index, col_index).value = getattr(row,x,None)
            row_index = row_index +1
        from openpyxl.writer.excel import save_virtual_workbook
        response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename= "{}"'.format("users.xlsx")
        return response


    except Exception as ex:
        quicky.sql_db.end_session(session)
        raise ex
    return ret

    return {}