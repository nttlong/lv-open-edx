def do_import(data):
    from django.contrib.auth.models import User
    from django.db import transaction
    from django.db.utils import IntegrityError
    import qexcel
    ret_error=[]

    i_row = 0

    for item in data:
        with transaction.atomic():
            users= User.objects.filter(username=item["username"])
            if users.__len__() == 0:
                user = User.objects.create_user(username=item["username"],
                                                email=item["email"],
                                                password=item.get("password",item["username"]))
            else:
                user=users[0]

            user.is_superuser = item.get("is_superuser", 0) == 1
            user.is_active = item.get("is_active", 0) == 1
            user.is_staff = item.get("is_staff", 0) == 1
            if item.get("first_name",None) != None:
                user.first_name = item.get("first_name")
            if item.get("first_name", None) != None:
                user.last_name = item.get("first_name")
            if item.get("email",None) != None:
                user.email = item.get("email",None)
            

            try:
                user.save()
                i_row = i_row + 1
            except IntegrityError as ex:
                ret_error.append(dict(
                    row=i_row,
                    message=ex.args[1]
                ))
                i_row = i_row + 1
            except Exception as ex:

                ret_error.append(dict(
                    row = i_row,
                    message = ex.message
                ))
                i_row = i_row + 1


    return ret_error