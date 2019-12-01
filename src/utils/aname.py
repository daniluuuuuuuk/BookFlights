from functools import singledispatch
from typing import Text

from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.db.models.query_utils import DeferredAttribute


@singledispatch
def a(obj) -> Text:
    return obj


@a.register
def _(obj: DeferredAttribute) -> Text:
    return obj.field_name


@a.register
def _(obj: ForwardManyToOneDescriptor) -> Text:
    return obj.field.name
