def do_import(data):
    from django.contrib.auth.models import User
    ret_error=[]

    for item in data:
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

        try:
            user.save()
        except Exception as ex:
            item.update({
                "error":ex.message
            })
            ret_error.append(item)

        print item
    return ret_error