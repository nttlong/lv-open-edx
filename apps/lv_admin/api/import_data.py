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
    wb = openpyxl.load_workbook(filename=filename,data_only=True)
    rows=list(wb.worksheets[0].rows)
    header_row=rows[0]
    data_list=[]
    for i in range(1,rows.__len__()):
        data_item={}
        for j in range(0,header_row.__len__()):
            data_item.update({
                header_row[j].value:rows[i][j].value
            })
        data_list.append(data_item)

    import importlib
    from quicky import applications
    app = applications.get_app_by_file(__file__)
    caller=importlib.import_module(app.package_name+".excel_import.{0}".format(args.data["objectType"]))
    ret=caller.do_import(data_list)

    return  ret