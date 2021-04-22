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
from blueapps.utils import get_client_by_request


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
@require_GET
def search_bussiness_topo(request):
    biz = int(request.GET['biz'][0])
    client = get_client_by_request(request)
    kwargs = {
        "bk_biz_id": biz
    }
    result = client.cc.search_biz_inst_topo(kwargs)
    data = modify_data(result['data'])
    return JsonResponse({"result": True, "data": data})


def modify_data(data):
    for inst in data:
        inst['children'] = inst['child']
        # inst['title'] = inst['bk_inst_name']
        inst['label'] = inst['bk_inst_name']
        inst['id'] = inst['bk_inst_id']
        if inst['child']:
            # inst['expand'] = True
            modify_data(inst['children'])
        # else:
        # inst['expand'] = False
    return data


@login_exempt
@csrf_exempt
@require_GET
def search_bussiness(request):
    client = get_client_by_request(request)
    # kwargs = {
    #     "bk_app_code": "general-baseline",
    #     "bk_app_secret": "b863c5ad-95db-4158-9eb5-416c1ade238d",
    #     "bk_username": "admin"
    # }
    result = client.cc.search_business()
    get_info = result['data']['info']
    return_data = [{'biz': inst['bk_biz_id'], 'name': inst['bk_biz_name']} for inst in get_info]
    return JsonResponse({"result": True, "data": return_data})


@csrf_exempt
@require_GET
def search_base_info(request):
    host = int(request.GET['host'][0])
    client = get_client_by_request(request)
    kwargs = {
        "bk_host_id": host,
    }
    result = client.cc.get_host_base_info(kwargs)
    return JsonResponse({"result": True, "data": result['data']})


# @login_exempt
# @require_GET
# def search_host_info(request):
#     client = get_client_by_request(request)
#     kwargs = {
#         "bk_app_code": "certmgmt",
#         "bk_app_secret": "fba3db9f-60a1-4c35-990c-3547aa183eb5",
#         "bk_username": "admin",
#         "bk_biz_id": 2,
#         "page": {
#             "start": 0,
#             "limit": 10
#         },
#         "fields": [
#             'bk_isp_name',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#             '',
#         ]
#     }
#     result = client.cc.list_biz_hosts(kwargs)
#     get_info = result['data']['info']
#     return_data = [{'biz': inst['bk_biz_id'], 'name': inst['bk_biz_name']} for inst in get_info]
#     return JsonResponse({"result": True, "data": return_data})


@login_exempt
@csrf_exempt
@require_POST
def query_detail(request):
    params = json.loads(request.body)
    page = params['page']
    page_size = params['page_size']
    biz = params['biz']
    query_params = params['params']
    client = get_client_by_request(request)
    if query_params['bk_obj_id'] != 'biz':
        kwargs = {
            "bk_biz_id": biz,
            "page": {
                "start": (page - 1) * page_size,
                "limit": page * page_size
            },
            "fields": [
                "bk_host_innerip"
            ],
            "bk_obj_id": query_params['bk_obj_id'],
            "bk_inst_id": int(query_params['bk_inst_id'])
        }
        result = client.cc.find_host_by_topo(kwargs)
        total = result['data']['count']
    else:
        kwargs = {
            "bk_biz_id": biz,
            "page": {
                "start": (page - 1) * page_size,
                "limit": page * page_size
            },
            "fields": [
                "bk_host_innerip"
            ]
        }
        result = client.cc.list_biz_hosts(kwargs)
        total = result['data']['count']
    temp_data = result['data']['info']
    ip_list = [{
        "field": "bk_host_innerip",
        "operator": "equal",
        "value": inst["bk_host_innerip"]
    } for inst in temp_data]
    kwargs = {
        "bk_biz_id": biz,
        "page": {
            "start": (page - 1) * page_size,
            "limit": page * page_size
        },
        "fields": [
            "bk_cloud_id",
            "bk_host_innerip",
            "operator",
            "bk_os_type",
            "bk_host_id"
        ],
        "host_property_filter": {
            "condition": "OR",
            "rules": ip_list
        }
    }
    result = client.cc.list_biz_hosts_topo(kwargs)
    temp_return_data = result['data']['info']
    return_data = []
    for host_inst in temp_return_data:
        temp_dict = {}
        temp_bk_set_name = []
        temp_bk_module_name = []
        for topo in host_inst['topo']:
            temp_bk_set_name.append(topo['bk_set_name'])
            for module in topo['module']:
                temp_bk_module_name.append(module['bk_module_name'])
        temp_dict['operator'] = host_inst['host']['operator']
        temp_dict['bk_os_type'] = 'Linux' if host_inst['host']['bk_os_type'] == "1" else "Windows" if host_inst['host'][
                                                                                                          'bk_os_type'] == "2" else "AIX"
        temp_dict['bk_set_name'] = list(set(temp_bk_set_name))
        temp_dict['bk_module_name'] = list(set(temp_bk_module_name))
        temp_dict['bk_host_id'] = host_inst['host']['bk_host_id']
        temp_dict['bk_cloud_id'] = host_inst['host']['bk_cloud_id']
        temp_dict['bk_host_innerip'] = host_inst['host']['bk_host_innerip']
        return_data.append(temp_dict)
    return JsonResponse({"result": True, "data": return_data, "total": total})
    # temp_data = result['data']['info']
    # for inst in temp_data:
    #     kwargs = {
    #         "bk_app_code": "certmgmt",
    #         "bk_app_secret": "fba3db9f-60a1-4c35-990c-3547aa183eb5",
    #         "bk_username": "admin",
    #         "bk_biz_id": biz,
    #         "bk_module_ids": [inst['bk_host_id']],
    #         "page": {
    #             "start": 0,
    #             "limit": 10
    #         },
    #     }
    #     result = client.cc.find_host_topo_relation(kwargs)
    #     temp_host_data = result['data']['info']


@login_exempt
@csrf_exempt
@require_POST
def search_host_list(request):
    params = json.loads(request.body)
    page = params['page']
    page_size = params['page_size']
    biz = params['biz']
    query_params = params['params']
    filter_params = params['filter']
    search_data = int(params['search_data']) if filter_params in ['bk_service_term', 'bk_os_bit', 'bk_host_id',
                                                                  'bk_disk', 'bk_cpu_mhz', 'bk_cpu', 'bk_cloud_id'] else \
        params['search_data']
    client = get_client_by_request(request)
    if query_params['bk_obj_name'] == '业务':
        kwargs = {
            "bk_biz_id": biz,
            "page": {
                "start": (page - 1) * page_size,
                "limit": page * page_size - 1
            },
            "fields": [
                "bk_host_innerip",
            ],
            "host_property_filter": {
                "condition": "AND",
                "rules": [{
                    "field": filter_params,
                    "operator": "equal",
                    "value": search_data
                }]
            }
        }
    elif query_params['bk_obj_name'] == '应用':
        set_inst_id = [inst['bk_inst_id'] for inst in query_params['children']]
        kwargs = {
            "bk_biz_id": biz,
            "page": {
                "start": (page - 1) * page_size,
                "limit": page * page_size - 1
            },
            "bk_set_ids": set_inst_id,
            "fields": [
                "bk_host_innerip",
            ],
            "host_property_filter": {
                "condition": "AND",
                "rules": [{
                    "field": filter_params,
                    "operator": "contains",
                    "value": search_data
                }]
            }
        }
    elif query_params['bk_obj_name'] == '集群':
        kwargs = {
            "bk_biz_id": biz,
            "page": {
                "start": (page - 1) * page_size,
                "limit": page * page_size - 1
            },
            "bk_set_ids": [query_params['bk_inst_id']],
            "fields": [
                "bk_host_innerip",
            ],
            "host_property_filter": {
                "condition": "AND",
                "rules": [{
                    "field": filter_params,
                    "operator": "contains",
                    "value": search_data
                }]
            }
        }
    else:
        kwargs = {
            "bk_biz_id": biz,
            "page": {
                "start": (page - 1) * page_size,
                "limit": page * page_size - 1
            },
            "bk_module_ids": [query_params['bk_inst_id']],
            "fields": [
                "bk_host_innerip",
            ],
            "host_property_filter": {
                "condition": "AND",
                "rules": [{
                    "field": filter_params,
                    "operator": "contains",
                    "value": search_data
                }]
            }
        }
    result = client.cc.list_biz_hosts(kwargs)
    get_info = result['data']['info']
    total = result['data']['count']
    ip_list = [{
        "field": "bk_host_innerip",
        "operator": "equal",
        "value": inst["bk_host_innerip"]
    } for inst in get_info]
    kwargs = {
        "bk_biz_id": biz,
        "page": {
            "start": (page - 1) * page_size,
            "limit": page * page_size
        },
        "fields": [
            "bk_cloud_id",
            "bk_host_innerip",
            "operator",
            "bk_os_type",
            "bk_host_id"
        ],
        "host_property_filter": {
            "condition": "OR",
            "rules": ip_list
        }
    }
    result = client.cc.list_biz_hosts_topo(kwargs)
    temp_return_data = result['data']['info']
    return_data = []
    for host_inst in temp_return_data:
        temp_dict = {}
        temp_bk_set_name = []
        temp_bk_module_name = []
        for topo in host_inst['topo']:
            temp_bk_set_name.append(topo['bk_set_name'])
            for module in topo['module']:
                temp_bk_module_name.append(module['bk_module_name'])
        temp_dict['operator'] = host_inst['host']['operator']
        temp_dict['bk_os_type'] = 'Linux' if host_inst['host']['bk_os_type'] == "1" else "Windows" if host_inst['host'][
                                                                                                          'bk_os_type'] == "2" else "AIX"
        temp_dict['bk_set_name'] = list(set(temp_bk_set_name))
        temp_dict['bk_module_name'] = list(set(temp_bk_module_name))
        temp_dict['bk_host_id'] = host_inst['host']['bk_host_id']
        temp_dict['bk_cloud_id'] = host_inst['host']['bk_cloud_id']
        temp_dict['bk_host_innerip'] = host_inst['host']['bk_host_innerip']
        return_data.append(temp_dict)
    return JsonResponse({"result": True, "data": return_data, "total": total})


@login_exempt
@csrf_exempt
@require_POST
def query_node_info(request):
    params = json.loads(request.body)
    biz = params['biz']
    query_params = params['params']
    client = get_client_by_request(request)
    kwargs = {
        "bk_obj_id": query_params['bk_obj_id'],
    }
    result = client.cc.search_object_attribute(kwargs)
    temp_list = []
    temp_group_list = []
    for property in result['data']:
        temp_dict = {}
        if property['bk_property_group_name'] not in temp_group_list:
            temp_group_list.append(property['bk_property_group_name'])
        temp_dict['key'] = property['bk_property_id']
        temp_dict['name'] = property['bk_property_name']
        temp_dict['group_id'] = temp_group_list.index(property['bk_property_group_name'])
        temp_list.append(temp_dict)
    if query_params['bk_obj_id'] == "biz":
        temp_conditionn = {"bk_biz_id": int(biz)}
    elif query_params['bk_obj_id'] == "set":
        temp_conditionn = {"bk_set_id": int(query_params['bk_inst_id'])}
    elif query_params['bk_obj_id'] == "module":
        temp_conditionn = {"bk_module_id": int(query_params['bk_inst_id'])}
    kwargs = {
        "bk_obj_id": query_params['bk_obj_id'],
        "fields": [],
        "condition": temp_conditionn
    }
    result = client.cc.search_inst_by_object(kwargs)
    data_info = result['data']['info'][0]
    for info in temp_list:
        info["value"] = data_info[info['key']] if data_info[info['key']] else "--"
    return_dict = {}
    for i, v in enumerate(temp_group_list):
        return_dict[v] = []
        for j in temp_list:
            if j['group_id'] == i:
                return_dict[v].append(j)
    for k, v in return_dict.items():
        slice_list = []
        for i in range(0, len(v), 3):
            get_slice = v[i:i + 3]
            slice_list.append(get_slice)
        return_dict[k] = slice_list
    return JsonResponse({"result": True, "title": temp_group_list, "data": return_dict})
    # return JsonResponse({"result": True, "data": return_dict})
