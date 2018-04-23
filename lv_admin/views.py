import quicky
@quicky.view.template("index.html")
def index(request):
    return request.render({})
