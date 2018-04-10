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
from edxmako.shortcuts import render_to_response
from lacviet.db.nosql import get_context
from xmodule.modulestore.split_mongo.mongo_connection import MongoConnection

def get_exam(request):
    connect = get_context();

    items = connect['modulestore.structures'].aggregate([
        {"$unwind": "$blocks"},
        {"$match": {"$and": [{"blocks.block_type": "problem"}, {"blocks.fields.markdown": {"$exists": "true"}},{"blocks.fields.markdown":{"$ne" : None}}]}},
        {"$group": {"_id": "$original_version", "data": {"$addToSet": "$blocks"}}}
    ])

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
                count += 1
            if check:
                arraysurvey.append(survery)

    context = {
        "data": arraysurvey,
        "count": len(arraysurvey)
    }
    return render_to_response("exam.html", context)