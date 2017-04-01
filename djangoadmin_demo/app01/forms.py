#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/28

"""
forms
"""
from django.forms import ModelForm


def its_new(cls, *args, **kwargs):
    for field_name in cls.base_fields:
        field = cls.base_fields[field_name]

        attr_dic = {"placeholder": field.help_text}

        if "BooleanField" not in field.__repr__():  # 如果没有布尔字段
            attr_dic.update({"class": "form-control"})

            if "ModelChoiceField" in field.__repr__():  # Foreign Key
                attr_dic.update({"data-tag": field_name})

        if cls.Meta.form_create is False:
            if field_name in cls.Meta.admin.readonly_fields:  # 给只读字段添加disable=True
                attr_dic["disable"] = True

        field.widget.attrs.update(attr_dic)  # 更新每个字段的样式
    print("model form class:", dir(cls.Meta))
    return ModelForm.__new__(cls)


def create_form(model, fields, admin_class, form_create=False):

    class Meta:
        pass

    setattr(Meta, "model", model)
    setattr(Meta, "fields", fields)
    setattr(Meta, "admin", admin_class)
    setattr(Meta, "form_create", form_create)

    attr = {"Meta": Meta}
    name = "DynamicModelForm"
    base_classes = (ModelForm, )
    # 创建动态的model form类
    model_form = type(name, base_classes, attr)
    setattr(model_form, "__new__", its_new)  # 添加__new__()方法
    print(model_form)

    return model_form
