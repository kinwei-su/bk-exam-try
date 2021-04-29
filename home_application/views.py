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
import time

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
def search_business(request):
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
    kwargs = json.loads(request.body)
    kwargs = {
        # 源文件主机参数
        "file_source": [
            {"account": source["account"], "ip_list": source["ip_list"], "files": [source["files"]]},
        ],
        # 目标服务器参数
        "bk_biz_id": int(target["bk_biz_id"]),
        "account": target["account"],
        "file_target_path": target["file_target_path"],
        "ip_list": target["ip_list"],
    }
    result = client.job.fast_push_file(kwargs)
    if result["result"]:
        task_id = result["data"]["job_instance_id"]
        time.sleep(2)
        rst_data = get_ip_log_content(client, int(target["bk_biz_id"]), task_id)
        if not rst_data["result"]:
            return {"result": False, "data": result["data"]}
        success_list = list({item["result"] for item in rst_data["data"]})
        success = True if len(success_list) == 1 and success_list[0] else False
        return {"result": success, "data": rst_data["data"]}
    else:
        return {"result": False, "data": result["message"]}



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


def get_ip_log_content(client, bk_biz_id, task_id, i=1, sleep_time=10):
    """
    获取作业平台执行结果日志信息
    :param client: 客户端
    :param bk_biz_id: 业务ID
    :param task_id: 任务ID
    :param i: 循环次数
    :param sleep_time: 每次获取结果日志循环等待时间（s）
    :return: 返回日志信息
    """
    kwargs = {"bk_biz_id": bk_biz_id, "job_instance_id": int(task_id)}
    result = client.job.get_job_instance_log(kwargs)
    if not result["result"]:
        i += 1
        if i > 5:
            return []
        time.sleep(10)
        return get_ip_log_content(client, bk_biz_id, task_id, i)
    if result["data"][0]["is_finished"]:
        log_content = []
        for i in result["data"][0]["step_results"]:
            log_content += [
                {
                    "ip": u["ip"],
                    "logContent": u["log_content"],
                    "bk_cloud_id": u["bk_cloud_id"],
                    "result": i["ip_status"] == 9,
                }
                for u in i["ip_logs"]
            ]
        return {"result": True, "data": log_content}
    time.sleep(sleep_time)
    return get_ip_log_content(client, bk_biz_id, task_id)

def fast_execute_script(
    executor,
    biz_id,
    ip_list,
    execute_account,
    script_content,
    script_type=1,
    param_content="",
    script_timeout=1000,
    task_name=None,
    is_param_sensitive=0,
    sleep_time=10,
):
    """
    快速执行脚本
    :param executor: 执行人，str
    :param biz_id: 业务ID，int
    :param ip_list: 操作主机, list, [{"ip":"10.0.0.10","bk_cloud_id":0}]
    :param execute_account: 脚本执行帐号，str
    :param script_content:  脚本执行内容，str
    :param script_type: 脚本类型，int
    :param param_content: 脚本参数，str，可不传，默认空字符串
    :param script_timeout: 超时时间，int，可不传，默认1000
    :param task_name: 任务名，默认为None
    :param is_param_sensitive: 是否敏感参数，0:否（默认），1:是
    :param sleep_time: 每次获取结果日志循环等待时间（s）
    :return:
    """
    client = get_client_by_user(executor)
    kwargs = {
        "bk_biz_id": biz_id,
        "script_content": base64.b64encode(script_content.encode("utf8")).decode("utf8"),
        "ip_list": ip_list,
        "script_type": script_type,
        "account": execute_account,
        "script_param": base64.b64encode(param_content.encode("utf8")).decode("utf8"),
        "script_timeout": script_timeout,
        "is_param_sensitive": is_param_sensitive,
    }
    if task_name:
        kwargs["task_name"] = task_name
    result = client.job.fast_execute_script(kwargs)
    if not result["result"]:
        return {"result": False, "data": result["message"]}
    return {
        "result": True,
        "data": get_ip_log_content(client, biz_id, result["data"]["job_instance_id"], sleep_time=sleep_time),
    }

def fast_execute_script_one_host(
    executor,
    biz_id,
    ip_list,
    execute_account,
    script_content,
    script_type=1,
    param_content="",
    script_timeout=1000,
    task_name=None,
    is_param_sensitive=0,
):
    """
    单个服务器快速执行
    :param executor:
    :param biz_id:
    :param ip_list:
    :param execute_account:
    :param script_content:
    :param script_type:
    :param param_content:
    :param script_timeout:
    :param task_name:
    :param is_param_sensitive:
    :return:
    """
    result = fast_execute_script(
        executor,
        biz_id,
        ip_list,
        execute_account,
        script_content,
        script_type=script_type,
        param_content=param_content,
        script_timeout=script_timeout,
        task_name=task_name,
        is_param_sensitive=is_param_sensitive,
    )

    if not (result["result"] and result["data"]["result"] and result["data"]["data"][0]["result"]):
        message = (
            result["data"]
            if not result["result"]
            else result["data"]["message"]
            if not result["data"]["result"]
            else result["data"]["data"][0]["logContent"].replace(MYSQL_PASSWORD_HINT, "").strip()
        )
        return False, message
    log_content = result["data"]["data"][0]["logContent"].replace(MYSQL_PASSWORD_HINT, "").strip()
    return True, log_content

# 命令行使用MySQL命令时的提示信息
MYSQL_PASSWORD_HINT = "mysql: [Warning] Using a password on the command line interface can be insecure."
