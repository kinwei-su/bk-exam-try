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

# from django.db import models
from django.db import models
# Create your models here.
from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    ignore_name = []  # 忽略字段，该字段不会使用to_dict转换，一般针对外键

    class Meta:
        abstract = True

    def to_dict(self):
        attrs = [f for f in self._meta.fields if f.name not in self.ignore_name]
        return_dict = {}
        for attr in attrs:
            if isinstance(attr, models.ForeignKey):
                return_dict["{}_{}".format(attr.name, "id")] = getattr(self, attr.name).id
                return_dict[attr.name] = getattr(self, attr.name).to_dict()
            elif isinstance(getattr(self, attr.name), datetime):
                return_dict[attr.name] = getattr(self, attr.name).strftime("%Y-%m-%d %H:%M:%S")
            elif attr.choices:
                return_dict["{}_{}".format(attr.name, "display")] = eval("self.get_{}_display()".format(attr.name))
                return_dict[attr.name] = getattr(self, attr.name)
            else:
                return_dict[attr.name] = getattr(self, attr.name)
        return return_dict

    def get_summary_title(self):
        fields = [item.name for item in self._meta.fields]
        key = self.name if "name" in fields else self.key if "key" in fields else ""
        summary_title = self._meta.verbose_name + "[{}]".format(key)
        return summary_title

    @property
    def get_key_items(self):
        key_items = [
            {"key": f.name, "name": f.verbose_name, "value": getattr(self, f.name), "is_list": False}
            for f in self._meta.fields
            if not (
                f.name in ["id", "modified_by", "create_by"]
                or isinstance(getattr(self, f.name), datetime)
                or isinstance(f, models.ForeignKey)
            )
        ]
        return key_items

    def get_add_detail(self):
        return self.get_key_items

    def get_delete_detail(self):
        return self.get_key_items

    def get_execute_detail(self):
        return self.get_key_items

    def get_update_detail(self, old_ins):
        detail = []
        now_item_list = self.get_key_items
        for i in now_item_list:
            now_value = i["value"]
            old_value = getattr(old_ins, i["key"])
            if now_value != old_value:
                value = "[{}] ==> [{}]".format(old_value, now_value)
                detail.append({"name": i["name"], "value": value, "is_list": False})
        return detail


class PublicFields(models.Model):
    remark = models.CharField(verbose_name="备注信息", max_length=1000)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    create_by = models.CharField(verbose_name="创建人", max_length=255)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    modified_by = models.CharField(verbose_name="修改人", max_length=255)

    class Meta:
        abstract = True


class Instance(BaseModel, PublicFields):
    name= models.CharField(verbose_name="实例名称", max_length=255, unique=True)
    host = models.CharField(verbose_name="主机IP", max_length=255, unique=True)
    port = models.CharField(verbose_name="端口", max_length=255)
    biz_name = models.CharField(verbose_name="业务名称", max_length=255)
    version = models.CharField(verbose_name="版本", max_length=255)
    status = models.CharField(verbose_name="部署状态", max_length=255)
    deploy_job = models.CharField(verbose_name="部署id", max_length=1000)
    delete_job = models.CharField(verbose_name="删除id", max_length=1000)

    class Meta:
        verbose_name = "实例信息"
