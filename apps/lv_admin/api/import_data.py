def import_from_excel(args):
    import binascii
    import struct
    import base64
    base64_content=args.data["content"]
    data = base64_content.split("base64,")[1]
    buffer_array=base64.decodestring(data)
    from io import BytesIO
    filename = BytesIO(buffer_array)
    import openpyxl
    from openpyxl import utils
    wb = openpyxl.load_workbook(filename=filename,data_only=True)
    data_sheet_items = [x for x in wb.worksheets if x.title == "data"]
    if data_sheet_items.__len__() == 0:
        return dict(
            error=dict(
                message="Data sheet was not found"
            )
        )
    list_of_col_name = list (wb.defined_names.definedName)
    rows=list(wb["data"].rows)
    header_row=[]
    for x in list_of_col_name:
        try:

            sheet_name=x.value.split('!')[0]
            if sheet_name == "data":
                col_adress =x.value.split("!")[1].split(':')[0].split('$')[1]
                header_row.append({
                    "name": x.name,
                    "index": utils.column_index_from_string(col_adress)-1
                })

        except Exception as ex:
            print ("{0} was not found".format(x.name))
    data_list=[]
    for i in range(1,rows.__len__()):
        data_item={}
        for j in range(0,header_row.__len__()):
            data_item.update({
                header_row[j]["name"]:rows[i][header_row[j]["index"]].value
            })
        data_list.append(data_item)

    import importlib
    from quicky import applications
    app = applications.get_app_by_file(__file__)
    caller=importlib.import_module(app.package_name+".excel_import.{0}".format(args.data["objectType"]))
    ret=caller.do_import(data_list)
    if ret.__len__() > 0:
        n_column = list(wb["data"].columns).__len__() + 1
        for x in ret:
            wb["data"].cell(x["row"]+1 , n_column).value = x["message"]
        from openpyxl.writer.excel import save_virtual_workbook
        import qexcel
        stm = save_virtual_workbook(wb)
        item = qexcel.get_coll_error().insert_one({"data":list(bytearray(stm))})
        msg=""
        msg_detail = args.request.get_app_res("Click <a href='{0}' target='_blank'>here<a> to download error file").format(
            args.request.get_app_url("excel/download_error/{0}").format(item.inserted_id.__str__())
        )
        if ret.__len__() == 1:
            msg = args.request.get_app_res("There is {0} error")
        else:
            msg = args.request.get_app_res("There are {0} errors")

        return dict(
            error=dict(
                message=msg.format(ret.__len__()),
                error_count =ret.__len__(),
                error_id = item.inserted_id.__str__(),
                msg_detail=msg_detail
            )
        )

    return  {}
