import json
import logging
import math
from functools import partial

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods, require_POST
from opaque_keys.edx.keys import AssetKey, CourseKey
from lacviet.db.nosql import get_context
from edxmako.shortcuts import render_to_response



from xmodule.modulestore.split_mongo.mongo_connection import MongoConnection

def get_survey(request):
    connect = get_context();

    items = connect['modulestore.structures'].aggregate([
        {"$unwind": "$blocks"},
        {"$match": {"$and": [{"blocks.block_type": "survey"}, {"blocks.fields.answers": {"$exists": "true"}}]}},
        {"$group": {"_id": "$original_version", "data": {"$addToSet": "$blocks"}}}
    ])
    countData = 0
    assets = list(items["result"])
    arraysurvey = []
    for item in assets:
        for survery in item["data"]:
            count = 0
            check = True
            for i in arraysurvey:
                if survery["block_id"] == i["block_id"]:
                    if survery["edit_info"]["edited_on"] > i["edit_info"]["edited_on"]:
                        arraysurvey[count] = survery
                    check = False
                count+=1
            if check:
                arraysurvey.append(survery)
    context = {
        "data":arraysurvey
    }
    return render_to_response("survey.html", context)