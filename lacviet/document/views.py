import json
import logging
import math
from functools import partial
from lacviet.db.nosql import get_context

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods, require_POST
from opaque_keys.edx.keys import AssetKey, CourseKey
from pymongo import ASCENDING, DESCENDING

from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.contentserver.caching import del_cached_content
from student.auth import has_course_author_access
from util.date_utils import get_default_time_display
from util.json_request import JsonResponse
from xmodule.contentstore.content import StaticContent
from xmodule.contentstore.mongo import MongoContentStore

from xmodule.exceptions import NotFoundError
from xmodule.modulestore.django import modulestore
from xmodule.modulestore.exceptions import ItemNotFoundError
import MySQLdb

__all__ = ['assets_document']

# pylint: disable=unused-argument


@login_required
@ensure_csrf_cookie
def get_document(request, course_key_string=None, asset_key_string=None):

        data = _assets_json(request, None)

        return render_to_response('asset_index.html',{"data":data})


def _assets_json(request, course_key):
    """
    Display an editable asset library.

    Supports starLoadingt (0-based index into the list of assets) and max query parameters.
    """
    requested_page = int(request.GET.get('page', 0))
    requested_page_size = int(request.GET.get('page_size', 50))
    requested_sort = request.GET.get('sort', 'date_added')
    requested_filter = request.GET.get('asset_type', '')
    requested_file_types = settings.FILES_AND_UPLOAD_TYPE_FILTERS.get(
        requested_filter, None)
    filter_params = None
    if requested_filter:
        if requested_filter == 'OTHER':
            all_filters = settings.FILES_AND_UPLOAD_TYPE_FILTERS
            where = []
            for all_filter in all_filters:
                extension_filters = all_filters[all_filter]
                where.extend(
                    ["JSON.stringify(this.contentType).toUpperCase() != JSON.stringify('{}').toUpperCase()".format(
                        extension_filter) for extension_filter in extension_filters])
            filter_params = {
                "$where": ' && '.join(where),
            }
        else:
            where = ["JSON.stringify(this.contentType).toUpperCase() == JSON.stringify('{}').toUpperCase()".format(
                req_filter) for req_filter in requested_file_types]
            filter_params = {
                "$where": ' || '.join(where),
            }

    sort_direction = DESCENDING
    if request.GET.get('direction', '').lower() == 'asc':
        sort_direction = ASCENDING

    # Convert the field name to the Mongo name
    if requested_sort == 'date_added':
        requested_sort = 'uploadDate'
    elif requested_sort == 'display_name':
        requested_sort = 'displayname'
    sort = [(requested_sort, sort_direction)]

    current_page = max(requested_page, 0)
    start = current_page * requested_page_size
    options = {
        'current_page': current_page,
        'page_size': requested_page_size,
        'sort': sort,
        'filter_params': filter_params
    }
    assets, total_count = _get_assets_for_page(request, course_key, options)
    end = start + len(assets)
    asset_json = []
    for asset in assets:
        asset_location = asset['asset_key']
        # note, due to the schema change we may not have a 'thumbnail_location'
        # in the result set
        thumbnail_location = asset.get('thumbnail_location', None)
        if thumbnail_location:
            if course_key is not None:
                thumbnail_location = course_key.make_asset_key(
                    'thumbnail', thumbnail_location[4])
            else:
                thumbnail_location = asset["courseKey"].make_asset_key(
                    'thumbnail', thumbnail_location[4])

        asset_locked = asset.get('locked', False)

        asset_json.append(_get_asset_json(
            asset['displayname'],
            asset['contentType'],
            asset['uploadDate'],
            asset_location,
            thumbnail_location,
            asset_locked,
            asset["name_creater"]
        ))
    # If the query is beyond the final page, then re-query the final page so
    # that at least one asset is returned

    data_document = {
        'start': start,
        'end': end,
        'page': current_page,
        'pageSize': requested_page_size,
        'totalCount': total_count,
        'assets': asset_json,
        'sort': requested_sort
    }
    return data_document


def _get_assets_for_page(request, course_key, options):
    """
    Returns the list of assets for the specified page and page size.
    """
    current_page = options['current_page']
    page_size = options['page_size']
    sort = options['sort']
    filter_params = options['filter_params'] if options['filter_params'] else None
    start = current_page * page_size
    connection = MongoContentStore("172.16.7.63","lv_lms",27017,True,"root","123456")

    return get_all(
        connection,start=start, maxresults=page_size, sort=sort, filter_params=filter_params
    )

def get_all(connection, start=0, maxresults=-1, sort=None, filter_params=None):
    connect = get_context()
    db = MySQLdb.connect(host="172.16.7.63",  # your host, usually localhost
                         port=3306,
                         user="root",  # your username
                         passwd="123456",  # your password
                         db="lv_lms")  # name of the data base
    cur = db.cursor()

    find_args = {"sort": sort}
    if maxresults > 0:
        find_args.update({
            "skip": start,
            "limit": maxresults,
        })
    items = connection.fs_files.find(**find_args)
    # items = connection["fs_files"].find(**find_args)
    count = items.count()
    assets = list(items)
    array_courses = []
    for item in assets:
        for course in array_courses:
            if item["content_son"]["course"]+item["content_son"]["org"]+item["content_son"]["run"] == course["id_course"]:
                item["name_creater"] = course["name"]
            else:
               info_user = connect["modulestore.active_versions"].find_one({"course": item["content_son"]["course"], "org":item["content_son"]["org"],"course":item["content_son"]["course"] })
               query = "SELECT name FROM bitnami_edxapp.auth_userprofile Where user_id = " + str(info_user["edited_by"])
               cur.execute(query)
               data = cur.fetchall()
               if data:
                   array_courses.append({
                       "id_course":item["content_son"]["course"]+item["content_son"]["org"]+item["content_son"]["run"],
                       "name": data[0][0]
                   })
                   item["name_creater"] = data[0][0]
               else:
                   item["name_creater"] = " "
        if len(array_courses) == 0:
            info_user = connect["modulestore.active_versions"].find_one(
                {"course": item["content_son"]["course"], "org": item["content_son"]["org"],
                 "course": item["content_son"]["course"]})
            query = "SELECT name FROM bitnami_edxapp.auth_userprofile Where user_id = " + str(info_user["edited_by"])
            cur.execute(query)
            data = cur.fetchall()
            if data:
                array_courses.append({
                    "id_course": item["content_son"]["course"] + item["content_son"]["org"] + item["content_son"]["run"],
                    "name": data[0][0]
                })
                item["name_creater"] = data[0][0]
            else:
                item["name_creater"] = " "
    cur.close()
    db.close()

    #u'asset-v1:edX+DemoX+Demo_Course+type@asset+block@L9_buckets.png'
    # We're constructing the asset key immediately after retrieval from the database so that
    # callers are insulated from knowing how our identifiers are stored.
    #/course-v1:edX+DemoX+Demo_Course/
    for asset in assets:
        asset_id = asset.get('content_son', asset['_id'])
        key = CourseKey.from_string("course-v1:" + asset_id["org"] + "+" + asset_id["course"] + "+" + asset_id["run"]);
        asset['asset_key'] = key.make_asset_key(asset_id['category'], asset_id['name'])
        asset["courseKey"] = key
    return assets, count

def _get_asset_json(display_name, content_type, date, location, thumbnail_location, locked,name_creater):
    """
    Helper method for formatting the asset information to send to client.
    """
    asset_url = StaticContent.serialize_asset_key_with_slash(location)
    external_url = 'localhost:8000' + asset_url
    return {
        'display_name': display_name,
        'content_type': content_type,
        'date_added': get_default_time_display(date),
        'url': asset_url,
        'external_url': external_url,
        'portable_url': StaticContent.get_static_path_from_location(location),
        'thumbnail': StaticContent.serialize_asset_key_with_slash(thumbnail_location) if thumbnail_location else None,
        'locked': locked,
        'name_creater':name_creater
    }
