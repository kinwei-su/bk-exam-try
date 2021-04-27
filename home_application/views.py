# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
from blueapps.account.decorators import login_exempt
from blueapps.utils import get_client_by_request, get_client_by_user
from home_application.models import Instance
from django.core.paginator import Paginator


def home(request):
    """
    首页
    """
    return render(request, "index.html")


@require_GET
def login_info(request):
    return JsonResponse(
        {"result": True, "data": {"username": request.user.username, "super": request.user.is_superuser}}
    )


@require_POST
def test_post(request):
    return JsonResponse({"result": True, "data": {}})


@require_GET
def test_get(request):
    return JsonResponse({"result": True, "data": {}})


@login_exempt
@csrf_exempt
@require_GET
def search_bussiness(request):
    """
    response
{
    "result": true,
    "data": [
        {
            "biz": 2,
            "name": "蓝鲸"
        }
    ]
}
    """
    client = get_client_by_request(request)
    result = client.cc.search_business()
    get_info = result['data']['info']
    return_data = [{'biz': inst['bk_biz_id'], 'name': inst['bk_biz_name']} for inst in get_info]
    return JsonResponse({"result": True, "data": return_data})


# 查询主机
@require_POST
@login_exempt
@csrf_exempt
def get_all_hosts(request):
    """
    request
    { "bk_biz_id": 3
    }
    response
    {
    "result": true,
    "data": [
        {
            "bk_os_type": "1",
            "bk_mac": "00:50:56:a0:3b:47",
            "bk_host_id": 7,
            "bk_cloud_id": 0,
            "bk_host_innerip": "192.168.165.175"
        }
    ],
    "remark": []
}
    """
    client = get_client_by_user("admin")
    args = json.loads(request.body)
    params = {
        'bk_biz_id': args["bk_biz_id"],
        "page": {
            "start": 0,
            "limit": 500,
            "sort": "bk_host_id"
        },
        "fields": [
        "bk_host_id",
        "bk_cloud_id",
        "bk_host_innerip",
        "bk_os_type",
        "bk_mac"
    ]
    }
    api_res = client.cc.list_biz_hosts(params)
    # print(api_res)
    # 拼装数据
    remark = []
    if api_res["result"]:
        return JsonResponse({"result": True, "data": api_res["data"]["info"], "remark": remark})
    else:
        return JsonResponse({"result": False, "message": "false"})

#分发文件
@require_POST
@login_exempt
@csrf_exempt
def fast_push_file(request):
    client = get_client_by_user("admin")
    args = json.loads(request.body)
    api_res = client.job.fast_push_file(args)

    if api_res["result"]:
        return JsonResponse({"result": True, "data": api_res["data"]["info"], "remark": remark})
    else:
        return JsonResponse({"result": False, "message": "false"})

# 查询参数
@require_GET
def search_instance(request):
    """所有参数都是可传可不传的，也可以默认传空
    request
    {
    "page":""
    "size":""
    "sort":""
    "biz_name":""
    "instance_ip":""
    "instance_name":""
    }
    response
    {
    "result": true,
    "data": {
        "count": 1,
        "items": [
            {
                "id": 1,
                "remark": "",
                "create_time": "0000-00-00 00:00:00.000000",
                "create_by": "",
                "modified_time": "0000-00-00 00:00:00.000000",
                "modified_by": "",
                "name": "like",
                "host": "192.168.169.116",
                "port": "3606",
                "biz_name": "蓝鲸",
                "version": "",
                "status": "",
                "deploy_job": "",
                "delete_job": ""
            }
        ]
    }
    """

    page = int(request.GET.get("page", 1))
    size = int(request.GET.get("size", 10))
    sort = request.GET.get("sort", "-id")
    biz_name = request.GET.get("biz_id","")
    instance_ip = request.GET.get("ip", "")
    instance_name = request.GET.get("name", "")
    params = {}
    if biz_name != "":
        params["biz_name"] = biz_name
    if instance_ip != "":
        params["instance_ip"] = instance_ip
    if instance_name != "":
        params["instance_name"] = instance_name
    params_set = Instance.objects.filter(**params).order_by(sort)

    data = Paginator(params_set, size)
    info = data.get_page(page)
    if not data.count:
        return JsonResponse({"result": True, "message": "no search data"})
    return JsonResponse({"result": True, "data": {"count": data.count, "items": [obj.to_dict() for obj in info]}})



